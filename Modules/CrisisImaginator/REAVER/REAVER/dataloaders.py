
from stead import get_stead
from generator import GenericGenerator
import seisbench.generate as sbg
from torch.utils.data import DataLoader

from seisbench.util import worker_seeding
import numpy as np

def get_dataloaders(batch_size=4, sampling_rate=100, window_size=400, overlap=70):
    train, dev, test = get_stead(sampling_rate)

    phase_dict = {
        "trace_p_arrival_sample": "P",
        "trace_s_arrival_sample": "S"
    }

    train_generator = GenericGenerator(train, window_size, overlap)
    dev_generator = GenericGenerator(dev, window_size, overlap)

    augmentations = [
        sbg.ChangeDtype(np.float32),
        sbg.ProbabilisticLabeller(label_columns=phase_dict, sigma=20, dim=0)
    ]

    train_generator.add_augmentations(augmentations)
    dev_generator.add_augmentations(augmentations)



    train_loader = DataLoader(train_generator, batch_size=batch_size, shuffle=True, num_workers=4, worker_init_fn=worker_seeding)
    dev_loader = DataLoader(dev_generator, batch_size=batch_size, shuffle=False, num_workers=4, worker_init_fn=worker_seeding)

    return train_loader, dev_loader
