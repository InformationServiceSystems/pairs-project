
from torch.utils.data import Dataset
import numpy as np



class GenericGenerator(Dataset):
    def __init__(self, dataset, window_size, overlap):
        """        
        :param use_mel_transform: Boolean, if True, transforms the waveform data to log Mel spectrogram.
        """
        self._augmentations = []
        self.dataset = dataset
        self.window_size = window_size
        self.overlap = overlap
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

        # Recursive application of augmentation processing methods
        for func in self._augmentations:
            func(state_dict)

        state_dict = self._clean_state_dict(state_dict)
        state_dict = self.add_extra_augmentation(state_dict)
        return state_dict

    def add_extra_augmentation(self,state_dict):
        state_dict['X'],state_dict['y']  = slice_into_windows(state_dict['X'],state_dict['y'],self.window_size ,self.overlap)
        return state_dict
    def _populate_state_dict(self, idx):
        return {"X": self.dataset.get_sample(idx)}
    
    
    def _clean_state_dict(self, state_dict):
        # Remove all metadata from the output
        state_dict = {k: v[0] for k, v in state_dict.items()}
        return state_dict


def normalize_window(window):
    
    for w in window:
        w -= np.mean(w)
        w /= np.std(w)
        w[np.isnan(w)] = 1e-5
        w[np.isinf(w)] = 1e-5     
    return window

def slice_into_windows(X, y, window_length, overlap_percent):
    """
    Slice two arrays into windows with specified length and overlap.

    Parameters:
    X, y: Input arrays of shape (3, 6000)
    window_length: Length of each window
    overlap_percent: Percentage of overlap between consecutive windows

    Returns:
    x_windows, y_windows: Lists of sliced windows from X and y respectively
    """
    X = normalize_window(X)
    
    step_size = window_length - int(window_length * overlap_percent / 100)
    number_of_windows = 1 + (X.shape[1] - window_length) // step_size

    x_windows = []
    y_windows = []
    

    for i in range(number_of_windows):
        start_index = i * step_size
        end_index = start_index + window_length
        x_windows.append(X[:, start_index:end_index])
        y_windows.append(y[:, start_index:end_index])
    return np.array(x_windows), np.array(y_windows)


