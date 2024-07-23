#!/usr/bin/env python
# coding: utf-8

# In[16]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seisbench.data as sbd
import seisbench.models as sbm
import seisbench.generate as sbg
from seisbench.util import worker_seeding

import torch
from torch.utils.data import DataLoader
from obspy.clients.fdsn import Client
from obspy import UTCDateTime

from torch.utils.data import Dataset

import librosa
import numpy as np
import matplotlib.pyplot as plt

# Get the val split of stead
data = sbd.STEAD(sampling_rate=100)
_, dev, _ = data.train_dev_test()
mask = dev.metadata["trace_category"] == 'earthquake_local' 
dev.filter(mask)


phase_dict = {
    "trace_p_arrival_sample": "P",
    "trace_s_arrival_sample": "S"
}



def compute_log_mel_spectrograms(data, sr=100, visualize=False):
    """
    Compute log Mel spectrograms for the given seismic data.
    
    Parameters:
    - data: 4D numpy array or tensor with shape (batch, 3, 3001) representing multiple instances of 3 channels of seismic data.
    - sr: Sample rate (default=100).
    - visualize: Whether to visualize the log Mel spectrograms (default=False).
    
    Returns:
    - log_mel_spectrograms_batch: 4D numpy array with shape (batch, 3, 60, 151) containing the log Mel spectrograms for each instance in the batch.
    """
    if torch.is_tensor(data):
        data = data.detach().cpu().numpy()
    
    # Placeholder for the batch of log Mel spectrograms
    log_mel_spectrograms_batch = []

    # Constants
    n_fft = 64
    fmin, fmax = 0, sr / 2
    frame_length = int(0.1 * sr)  
    hop_length = frame_length // 4 

    # Process each instance in the batch
    for batch_index in range(data.shape[0]):
        log_mel_spectrograms = []
        for channel_index in range(data.shape[1]):
            # Extract the data for the current channel
            channel_data = data[batch_index, channel_index, :]

            # Compute the STFT with 64 bins (zero padded) and a Hamming window
            stft_result = librosa.stft(channel_data, n_fft=n_fft, win_length=frame_length, hop_length=hop_length, window='hamming')

            # Create Mel filter bank
            mel_filter_bank = librosa.filters.mel(sr=sr, n_fft=n_fft, n_mels=60, fmin=fmin, fmax=fmax)

            # Apply Mel filter bank to the magnitude spectrum
            mel_spectrogram = np.dot(mel_filter_bank, np.abs(stft_result))

            # Convert to log magnitude
            log_mel_spectrogram = np.log(mel_spectrogram + 1e-10)  # Adding a small constant to avoid log(0)
            
            # Append the log Mel spectrogram for the current channel to the list
            log_mel_spectrograms.append(log_mel_spectrogram)

            # Optional: visualize the log Mel spectrogram
            if visualize and batch_index == 0:  # Visualize only for the first instance in the batch
                plt.figure(figsize=(10, 4))
                librosa.display.specshow(log_mel_spectrogram, y_axis='mel', x_axis='time', sr=sr, hop_length=hop_length)
                plt.colorbar(format='%+2.0f dB')
                plt.title(f'Log Mel Spectrogram - Batch {batch_index}, Channel {channel_index}')
                plt.tight_layout()
                plt.show()

        # Stack the log Mel spectrograms for this instance
        log_mel_spectrograms_stacked = np.stack(log_mel_spectrograms)
        # Append to the batch
        log_mel_spectrograms_batch.append(log_mel_spectrograms_stacked)

    # Convert list to numpy array
    log_mel_spectrograms_batch = np.array(log_mel_spectrograms_batch)

    return log_mel_spectrograms_batch




def normalize_window(window):
    
    for w in window:
        w -= np.mean(w)
        w /= np.std(w)
        w[np.isnan(w)] = 1e-5
        w[np.isinf(w)] = 1e-5     
    return window

def slice_into_windows(X, y, window_length, overlap_percent):
    """
    Slice two arrays into windows with specified length and overlap, and return
    the start and end indices for each window.

    Parameters:
    X, y: Input arrays of shape (3, 6000)
    window_length: Length of each window
    overlap_percent: Percentage of overlap between consecutive windows

    Returns:
    x_windows, y_windows: Arrays of sliced windows from X and y respectively
    start_indices, end_indices: Arrays of start and end indices for each window
    """
    X = normalize_window(X)
    
    step_size = window_length - int(window_length * overlap_percent / 100)
    number_of_windows = 1 + (X.shape[1] - window_length) // step_size

    x_windows, y_windows = [], []
    start_indices, end_indices = [], []
    
    for i in range(number_of_windows):
        start_index = i * step_size
        end_index = start_index + window_length
        x_windows.append(X[:, start_index:end_index])
        y_windows.append(y[:, start_index:end_index])
        start_indices.append(start_index)
        end_indices.append(end_index)

    return (np.array(x_windows), np.array(y_windows), 
            np.array(start_indices), np.array(end_indices))



import numpy as np

def pad_array_zeros(arr, target_length):
    """
    Pads the given array 'arr' from the left with zeros to achieve the 'target_length'.
    """
    # Calculate the amount of padding needed
    padding_length = target_length - arr.shape[1]

    # Check if padding is needed
    if padding_length > 0:
        # Create a zero-filled array for the padding
        padding = np.zeros((arr.shape[0], padding_length))

        # Concatenate the padding to the left of the original array
        padded_arr = np.concatenate((padding, arr), axis=1)
        return padded_arr
    else:
        # If the array is already at or exceeds the target length, return it as is
        return arr



def pad_array(arr, target_length):

    padding_length = target_length - arr.shape[1]

    if padding_length > 0 and arr.shape[1] >= 5:
        repeat_times = (padding_length + 4) // 5  # Calculate how many times to repeat
        padding = np.tile(arr[:, :5], (1, repeat_times))[:, :padding_length]

        padded_arr = np.concatenate((padding, arr), axis=1)
        return padded_arr
    else:
        return arr




class GenericGenerator(Dataset):
    def __init__(self, dataset, window_length, overlab, padding = None):
        """        
        :param use_mel_transform: Boolean, if True, transforms the waveform data to log Mel spectrogram.
        """
        self.window_length = window_length
        self.overlab = overlab
        self.padding = padding
        self._augmentations = []
        self.dataset = dataset
        super().__init__()

    
    def augmentation(self, f):
        """
        Decorator for augmentations.
        """
        self._augmentations.append(f)

        return f

    def add_augmentations(self, augmentations):
        """
        Adds a list of augmentations to the generator. Can not be used as decorator.

        :param augmentations: List of augmentations
        :type augmentations: list[callable]
        """
        if not isinstance(augmentations, list):
            raise TypeError(
                "The argument of add_augmentations must be a list of augmentations."
            )

        self._augmentations.extend(augmentations)

    def __str__(self):
        summary = f"{self.__class__} with {len(self._augmentations)} augmentations:\n"
        for i, aug in enumerate(self._augmentations):
            summary += f" {i + 1}.\t{str(aug)}\n"
        return summary

    def __len__(self):
        return len(self.dataset)

    def __iter__(self):
        return self

    def __getitem__(self, idx):
        state_dict = self._populate_state_dict(idx)
        arrival_p = (state_dict['X'][1]['trace_p_arrival_sample'])
        arrival_s = (state_dict['X'][1]['trace_s_arrival_sample'])

        # Recursive application of augmentation processing methods
        for func in self._augmentations:
            func(state_dict)

        state_dict = self._clean_state_dict(state_dict)
        state_dict = self.add_extra_augmentation(state_dict, arrival_p, arrival_s)
        return state_dict

    def add_extra_augmentation(self,state_dict,arrival_p, arrival_s):
        if self.padding is not None:
            state_dict['X'],state_dict['y'] = pad_array(state_dict['X'], self.padding), pad_array(state_dict['y'], self.padding)
        state_dict['X'],state_dict['y'],state_dict['Start'], state_dict['End']   = slice_into_windows(state_dict['X'],state_dict['y'],self.window_length,self.overlab )
        state_dict['arrival_p'] = arrival_p
        state_dict['arrival_s'] = arrival_s
 
        return state_dict
    def _populate_state_dict(self, idx):
        return {"X": self.dataset.get_sample(idx)}
    
    
    def _clean_state_dict(self, state_dict):
        # Remove all metadata from the output
        
        state_dict = {k: v[0] for k, v in state_dict.items()}
        return state_dict



# select relevant windows for evaluation
def find_relevant_windows(sample, number):
    # Finding the window in which the number falls
    relevant_window_index = None

    for i in range(len(sample["Start"][0])):
        if sample["Start"][0][i] <= number < sample["End"][0][i]:
            relevant_window_index = i
            break

    # If the number doesn't fall in any window
    if relevant_window_index is None:
        return None

    # Calculating the indices 
    start_index = max(0, relevant_window_index - 3)
    end_index = min(len(sample["Start"][0]) - 1, relevant_window_index + 40)

    # Selecting the relevant windows for evaluation
    relevant_windows = [i for i in range(start_index, end_index + 1)]

    return relevant_windows


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



Window_length = 400 # 4 seconds window

model = REAVER(phases="PSN", norm="std")
model.load_state_dict(torch.load('../REAVER/model_epoch_iter_7000180.pth', map_location='cpu'))
model.eval();



dev_generator = GenericGenerator(dev, Window_length, 99, None)

augmentations = [
    sbg.ChangeDtype(np.float32),
    sbg.ProbabilisticLabeller(label_columns=phase_dict, sigma=20, dim=0)
]

dev_generator.add_augmentations(augmentations)




dev_loader = DataLoader(dev_generator, batch_size=1, shuffle=False, num_workers=2, worker_init_fn=worker_seeding)




from tqdm import tqdm

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

results = []
with open('results.txt', 'a') as f:
    for batch_id, sample in enumerate(dev_loader):
        print('Processing sample {}'.format(batch_id))

        # Ensure the data is on the GPU
        sample['X'] = sample['X'].to(device).reshape(-1, 3, 400)
        sample['y'] = sample['y'].to(device).reshape(-1, 3, 400)
        
        real_p_arrival = sample['arrival_p']
        real_s_arrival = sample['arrival_s']

        p_windows = find_relevant_windows(sample, real_p_arrival)
        s_windows = find_relevant_windows(sample, real_s_arrival)

        p_wave_detected = False
        s_wave_detected = False
        p_index = None
        s_index = None
        time_p = None
        time_s = None
        # Prepare batch
        all_windows = p_windows + s_windows


        batch_data = torch.stack([sample["X"][i, :, :].unsqueeze(0) for i in all_windows]).squeeze(1)
        batch_data_mel = torch.tensor(compute_log_mel_spectrograms(batch_data)).to(device)


        # Model inference on the entire batch
        with torch.no_grad():
            batch_pred_p, batch_pred_s = model(batch_data_mel)
        batch_pred_p = batch_pred_p.detach().cpu().numpy()
        batch_pred_s = batch_pred_s.detach().cpu().numpy()

        # Iterate through predictions for detection
        for idx, i in enumerate(all_windows):
            pred_p = batch_pred_p[idx]
            pred_s = batch_pred_s[idx]
            # check for p wave
            if i in p_windows and np.max(pred_p) > 0.7 and not p_wave_detected:
                p_wave_detected = True
                p_index = i
                time_p = sample["End"][0][i]
            # check for s wave
            if i in s_windows and np.max(pred_s) > 0.7 and not s_wave_detected:
                s_wave_detected = True
                s_index = i
                time_s = sample["End"][0][i]

            # Check if both waves are detected to potentially break early
            if p_wave_detected and s_wave_detected:
                break

        # Storing and writing results
        result = (batch_id, real_p_arrival, time_p, p_index, real_s_arrival, time_s, s_index)
        print(result)
        results.append(result)
        f.write(f'{result}\n')
        f.flush()


