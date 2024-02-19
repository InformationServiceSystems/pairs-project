import streamlit as st
from obspy import read_inventory
from datetime import datetime, timezone, timedelta
from obspy.clients.fdsn import Client
from obspy import UTCDateTime
import pandas as pd
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import time
import matplotlib.pyplot as plt
import numpy as np
from model import *
import torch
import obspy
from melspectogram import *






# Load the data
eq_data = pd.read_csv('../final_selected_EQs.csv')
waveforms = np.load('../final_selected_EQs.npy', allow_pickle=True)

# Streamlit page configuration
st.set_page_config(page_title='Real-Time EQ Prediction', layout='wide')

from streamlit_folium import st_folium
import folium



# Create a new column in the dataframe for the dropdown label
eq_data['dropdown_label'] = eq_data.apply(lambda row: f"ID: {row['index']} - {row['station_code']} at {row['source_origin_time']} (Mag: {row['source_magnitude']})", axis=1)

# Sidebar dropdown to select an earthquake
selected_label = st.sidebar.selectbox('Select an Earthquake', eq_data['dropdown_label'].values)
selected_index = eq_data[eq_data['dropdown_label'] == selected_label].index[0]
selected_eq = eq_data.loc[selected_index]
sample = waveforms[selected_index]

# Sidebar button to run the model
if st.sidebar.button('Run the model'):
    model = REAVER(phases="PSN", norm="std")
    model.load_state_dict(torch.load('../REAVER/model_checkpoints/checkpoint.pth', map_location='cpu'))
    model.eval();
    pred_npts = 400  # Size of the prediction window
    n_slices = len(sample["X"])



    # Set up the figure and axes
    fig, axs = plt.subplots(4, 1, figsize=(15, 8.5))
    # Plot the full data for each channel
    colors = ['red', 'green', 'blue']
    channel_names = ['Z', 'N', 'E']
    for i in range(3):
        axs[i].plot(sample['X_original'][i], color=colors[i])
        #axs[i].set_title(channel_names[i])
        axs[i].set_ylabel('Amplitude {}'.format(channel_names[i]))
        axs[i].grid(True)


    # Store inset axes for later removal
    inset_axes_list = [[None for _ in range(3)] for _ in range(n_slices)]

    text_placeholder = st.empty()
    plot_placeholder = st.empty()
    
    # Loop through the data
    p_wave_detected = False
    s_wave_detected = False
    for i in range(n_slices):

        current_window_data = sample["X"][i] 

        
        #log_mel_spectrograms_stacked = spectogram_class(torch.tensor(current_window_data)).detach().cpu().numpy()
        log_mel_spectrograms_stacked = compute_log_mel_spectrograms(torch.tensor(current_window_data).unsqueeze(0).detach().cpu().numpy())
        log_mel_spectrograms_stacked = torch.tensor(log_mel_spectrograms_stacked) 

        with torch.no_grad():
            pred_p, pred_s = model(log_mel_spectrograms_stacked)
            pred = torch.cat((pred_p, pred_s), 0)
        # Plotting 'pred' on the first row for the current window
        axs[-1].clear()  # Clear the previous predictions
        axs[-1].set_ylabel('Prediction Probability')
        axs[-1].set_ylim(0, 1)  # Setting y-axis limits from 0 to 1
        axs[-1].grid(True)
        #pred[:,0:100] = pred[:,0:100] * 0.5

        for j in range(pred.shape[0]):
            if j == 0:
                axs[-1].plot(np.linspace(0, pred_npts, pred_npts), pred[j], label=f'P-wave')
            else:
                axs[-1].plot(np.linspace(0, pred_npts, pred_npts), pred[j], label=f'S-wave')
        axs[-1].legend(loc='best')
        
        # Overlay the window and plot Mel spectrogram
        for j in range(3):
            ax = axs[j]
            # Remove the old inset axis if it exists
            if inset_axes_list[i-1][j] is not None:
                inset_axes_list[i-1][j].remove()
                inset_axes_list[i-1][j] = None  # Clear the reference

            # Create new inset for Mel spectrogram
            inset_ax = inset_axes(ax, width="100%", height="100%", 
                                bbox_to_anchor=(sample["Start"][i], ax.get_ylim()[0], 
                                                sample["End"][i] - sample["Start"][i], 
                                                ax.get_ylim()[1] - ax.get_ylim()[0]), 
                                bbox_transform=ax.transData, borderpad=0)
            librosa.display.specshow(log_mel_spectrograms_stacked.numpy()[0][j], 
                                    sr=100, hop_length=20, ax=inset_ax, 
                                    x_axis='time', y_axis='mel', zorder=2)
            inset_ax.axis('off')

            # Store the new inset axis
            inset_axes_list[i][j] = inset_ax

            # Display the plot in Streamlit
        #plt.tight_layout()
        plt.subplots_adjust(hspace=0.2)  # Change the value to increase/decrease the space

        plot_placeholder.pyplot(fig, use_container_width=True)  # This will scale the plot
        print(pred_p.shape, torch.max(pred_p[0, 250:]))
        if torch.max(pred_p[0, 250:]) > 0.7 and not p_wave_detected:
            text_placeholder.markdown('<p style="text-align: center; font-weight: bold; font-size: 24px;">Status: <span style="color: red;">P-wave detected! 🚨📢</span></p>', unsafe_allow_html=True)
            p_wave_detected = True
            time.sleep(2)
        if torch.max(pred_s[0, 250:]) > 0.7 and not s_wave_detected:
            s_wave_detected = True
            text_placeholder.markdown('<p style="text-align: center; font-weight: bold; font-size: 24px;">Status: <span style="color: red;">S-wave detected! 🚨📢</span></p>', unsafe_allow_html=True)
            time.sleep(2)
        elif p_wave_detected and not s_wave_detected:
            text_placeholder.markdown('<p style="text-align: center; font-weight: bold; font-size: 24px;">Earthquake happening. S-wave is coming! ⚠️</p>', unsafe_allow_html=True)
        elif torch.max(pred_s) < 0.2  and torch.max(pred_p) < 0.2 :
            text_placeholder.markdown('<p style="text-align: center; font-weight: bold; font-size: 24px;">Status: All Clear 🟢</p>', unsafe_allow_html=True)
