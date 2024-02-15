import seisbench.data as sbd
import seisbench.generate as sbg
import seisbench.models as sbm
from seisbench.util import worker_seeding

import numpy as np
import matplotlib.pyplot as plt
import torch
from torch.utils.data import DataLoader
from obspy.clients.fdsn import Client
from obspy import UTCDateTime




import json

import numpy as np
import scipy.signal
import torch
import torch.nn as nn
import torch.nn.functional as F
from packaging import version

import seisbench.util as sbu

from seisbench.models.base import Conv1dSame, WaveformModel, _cache_migration_v0_v3



class REAVER(WaveformModel):

    def __init__(self, in_channels=3, n_classes=1, phases="PSN", sampling_rate=100, norm="std", bilinear=True, **kwargs):
        # Apply pre-set options
        for option in ["norm_amp_per_comp", "norm_detrend"]:
            setattr(self, option, kwargs.pop(option, False))

        super().__init__(in_samples=400, output_type="array", pred_sample=(0, 400),
                         labels=phases, sampling_rate=sampling_rate, **kwargs)

        self.in_channels = in_channels
        self.n_classes = n_classes
        self.bilinear = bilinear
        self.global_avg_pool = nn.AdaptiveAvgPool2d((1, None))
        self.upsample = nn.Upsample(size=(1, 400), mode='bilinear', align_corners=True)

        # Spatial Attention and Upscaling layers for Task 1 and Task 2
        self.sa1_task1, self.sa2_task1, self.sa3_task1, self.sa4_task1 = [SABlock(size, size) for size in [512, 256, 128, 64]]
        self.sa1_task2, self.sa2_task2, self.sa3_task2, self.sa4_task2 = [SABlock(size, size) for size in [512, 256, 128, 64]]

        # Downscaling layers
        self.inc = DoubleConv(in_channels, 64)
        self.down1 = Down(64, 128)
        self.down2 = Down(128, 256)
        self.down3 = Down(256, 512)
        factor = 2 if bilinear else 1
        self.down4 = Down(512, 1024 // factor)

        # Upscaling layers
        self.up1 = Up(1024, 512 // factor, bilinear)
        self.up2 = Up(512, 256 // factor, bilinear)
        self.up3 = Up(256, 128 // factor, bilinear)
        self.up4 = Up(128, 64, bilinear)

        # Output convolution layers for Task 1 and Task 2
        self.outc_t1 = OutConv(64, n_classes)
        self.outc_t2 = OutConv(64, n_classes)

        self.sig = torch.nn.Sigmoid()

    def forward(self, x):
        x1 = self.inc(x)
        x2 = self.down1(x1)
        x3 = self.down2(x2)
        x4 = self.down3(x3)
        x5 = self.down4(x4)

        # Task 1: P-wave processing
        xt1 = self.process_task(x1, x2, x3, x4, x5, task=1)

        # Task 2: S-wave processing
        xt2 = self.process_task(x1, x2, x3, x4, x5, task=2)

        return self.sig(xt1).squeeze(1), self.sig(xt2).squeeze(1)

    def process_task(self, x1, x2, x3, x4, x5, task):
        # Select the appropriate spatial attention layers based on the task
        sa_layers = [self.sa1_task1, self.sa2_task1, self.sa3_task1, self.sa4_task1] if task == 1 else \
                    [self.sa1_task2, self.sa2_task2, self.sa3_task2, self.sa4_task2]

        x4_task = sa_layers[0](x4)
        x3_task = sa_layers[1](x3)
        x2_task = sa_layers[2](x2)
        x1_task = sa_layers[3](x1)

        # Upscaling and merging
        xt = self.up1(x5, x4_task)
        xt = self.up2(xt, x3_task)
        xt = self.up3(xt, x2_task)
        xt = self.up4(xt, x1_task)

        # Final output layer for the task
        out_conv = self.outc_t1 if task == 1 else self.outc_t2
        xt = out_conv(xt)
        xt = self.global_avg_pool(xt)
        xt = self.upsample(xt).squeeze(2)

        return xt


class DoubleConv(nn.Module):
    """(convolution => [BN] => ReLU) * 2"""

    def __init__(self, in_channels, out_channels, mid_channels=None):
        super().__init__()
        if not mid_channels:
            mid_channels = out_channels
        self.double_conv = nn.Sequential(
            nn.Conv2d(in_channels, mid_channels, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(mid_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(mid_channels, out_channels, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True)
        )

    def forward(self, x):
        return self.double_conv(x)


class Down(nn.Module):
    """Downscaling with maxpool then double conv"""

    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.maxpool_conv = nn.Sequential(
            nn.MaxPool2d(2),
            DoubleConv(in_channels, out_channels)
        )

    def forward(self, x):
        return self.maxpool_conv(x)


class Up(nn.Module):
    """Upscaling then double conv"""

    def __init__(self, in_channels, out_channels, bilinear=True):
        super().__init__()

        # if bilinear, use the normal convolutions to reduce the number of channels
        if bilinear:
            self.up = nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True)
            self.conv = DoubleConv(in_channels, out_channels, in_channels // 2)
        else:
            self.up = nn.ConvTranspose2d(in_channels, in_channels // 2, kernel_size=2, stride=2)
            self.conv = DoubleConv(in_channels, out_channels)

    def forward(self, x1, x2):
        x1 = self.up(x1)
        # input is CHW
        diffY = x2.size()[2] - x1.size()[2]
        diffX = x2.size()[3] - x1.size()[3]

        x1 = F.pad(x1, [diffX // 2, diffX - diffX // 2,
                        diffY // 2, diffY - diffY // 2])

        x = torch.cat([x2, x1], dim=1)
        return self.conv(x)


class OutConv(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(OutConv, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=1)

    def forward(self, x):
        return self.conv(x)

class SABlock(nn.Module):
    """ Spatial self-attention block """
    def __init__(self, in_channels, out_channels):
        super(SABlock, self).__init__()
        self.attention = nn.Sequential(nn.Conv2d(in_channels, out_channels, 3, padding=1, bias=False),
                                        nn.Sigmoid())
        self.conv = nn.Conv2d(in_channels, out_channels, 3, padding=1, bias=False)

    def forward(self, x):
        attention_mask = self.attention(x)
        features = self.conv(x)
        return torch.mul(features, attention_mask)

