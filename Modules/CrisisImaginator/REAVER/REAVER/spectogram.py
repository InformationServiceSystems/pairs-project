
import librosa
import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import librosa
import matplotlib.pyplot as plt
import torch

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