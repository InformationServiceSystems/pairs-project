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







# Streamlit page configuration
st.set_page_config(page_title='Real-Time EQ Prediction', layout='wide')


from streamlit_folium import st_folium
import folium
# Function to create and display the map
def display_map(latitude, longitude, station_code):
    # Create a map centered at the selected station
    m = folium.Map(location=[latitude, longitude], zoom_start=9)

    # Add a marker for the selected station
    tooltip = "Station: {}".format(station_code)
    folium.Marker(
        [latitude, longitude - 0.4], 
        popup=f"<i>{station_code}</i>", 
        tooltip=tooltip
    ).add_to(m)

    # Display the map in the Streamlit app
    st_folium(m, width=750, height=350)



def reorder_to_zne(stream):
    # Initialize variables to hold the indices
    index_z = index_n = index_e = None

    # Loop through each trace in the stream
    for i, trace in enumerate(stream):
        # Get the last character of the channel name
        channel_type = trace.stats.channel[-1]  # Assuming channel names are stored in trace.stats.channel

        # Check the last character and assign the index accordingly
        if channel_type == 'Z':
            index_z = i
        elif channel_type == 'N'  or channel_type == '1':
            index_n = i
        elif channel_type == 'E' or  channel_type == '2':
            index_e = i

    # Initialize an empty list for the ordered stream
    stream_zne = obspy.Stream()

    # Add the traces in ZNE order if they exist
    if index_z is not None:
        stream_zne.append(stream[index_z])
    if index_n is not None:
        stream_zne.append(stream[index_n])
    if index_e is not None:
        stream_zne.append(stream[index_e])

    # Now stream_zne is your stream with channels in ZNE order

    return stream_zne


model = REAVER(phases="PSN", norm="std")
model.load_state_dict(torch.load('../REAVER/model_checkpoints/checkpoint.pth', map_location='cpu'))
model.double();
model.eval();
# Check if the inventory is already loaded
if 'inventory' not in st.session_state:
    # Read the inventory from the file only if it's not already loaded
    st.session_state.inventory = read_inventory('inventory.xml')


# Sidebar for input parameters
st.sidebar.header('Input Parameters')

# Extract networks and their codes
networks = [net.code for net in st.session_state.inventory.networks]
selected_network = st.sidebar.selectbox("Network", networks)

# Find the selected network in the inventory
network = st.session_state.inventory.select(network=selected_network)[0]

# Extract stations and their codes from the selected network
stations = {station.code: station for station in network}

# Use a selectbox to choose a station
selected_station_code = st.sidebar.selectbox("Station", list(stations.keys()))

# Access the selected station object
selected_station = stations[selected_station_code]

# Access latitude and longitude of the selected station
latitude = selected_station.latitude
longitude = selected_station.longitude

# You can print or display the location
print(f"Location of station {selected_station_code}: Latitude {latitude}, Longitude {longitude}")

# Assuming you want to use the first location (modify as needed)
# If locations vary and you want to list them, you will need additional logic here
selected_location = '*'
start_button = st.sidebar.button('Start Monitoring')



# Initialize or reset the monitoring state when the button is pressed
if start_button:
    st.session_state.monitoring = True
    st.session_state.start_time = datetime.now(timezone.utc) - timedelta(seconds=180)
    st.session_state.end_time = datetime.now(timezone.utc) - timedelta(seconds=150)

# Ensure the block only runs if monitoring is set to True
if st.session_state.get('monitoring', False):
    
    p_wave_detected = False
    s_wave_detected = False
    client = Client("IRIS")
    st.subheader("Monitoring station {}, located at lat: {} and long: {}".format(selected_station_code, latitude, longitude))
    col1, col2 = st.columns([2, 1])
    with col2:
        display_map(selected_station.latitude, selected_station.longitude, selected_station_code)
        text_placeholder = st.empty()
    with col1:
        plot_placeholder_2 = st.empty()
        while True:
            
            
            # Calculate new time range
            st.session_state.start_time += timedelta(seconds=1)
            st.session_state.end_time += timedelta(seconds=1)

            start = st.session_state.start_time.strftime("%Y-%m-%dT%H:%M:%SZ")
            end = st.session_state.end_time.strftime("%Y-%m-%dT%H:%M:%SZ")

            print(start, end)
            # Define the time range for the data
            start_time = UTCDateTime(start)
            end_time = UTCDateTime(end)

            # Define station parameters
            channels = ['HNZ', 'HNN', 'HNE']  # Z, N, and E components
            # Try to fetch waveform data for each component
            try:
                stream = client.get_waveforms(selected_network, selected_station_code, selected_location, ",".join(channels), start_time, end_time)
                stream = stream.detrend("demean")
                stream = stream.filter("bandpass", freqmin=1, freqmax=45)
                stream = stream.taper(max_percentage=0.005)
                stream = stream[0:3].resample(100)
                stream = reorder_to_zne(stream)
                if len(stream) != 3:
                    raise Exception
                print(stream)
            except Exception as e:
                st.error(f"Error fetching waveforms: {e} Please try another station.")
                break

            # Set up the figure and axes
            fig, axs = plt.subplots(4, 1, figsize=(15, 10))

            # Define channel names and colors for the plot
            channel_names = ['Z', 'N', 'E']
            colors = ['red', 'green', 'blue']

            for i, (ax, channel, color) in enumerate(zip(axs, channel_names, colors)):
                channel_data = stream[i].data  # Replace with appropriate data source

                # Convert to Pandas DataFrame for plotting
                df = pd.DataFrame({
                    'Amplitude': channel_data
                })

                # Plot the data
                ax.plot(df['Amplitude'], color=color)

                # Set individual plot titles and labels
                ax.set_title(channel, fontsize='large', loc='left', pad=-15)
                ax.set_ylabel('Amplitude')

                # Set grid
                ax.grid(True, which='both', linestyle='--', linewidth=0.5)

                # Set the y-axis limits based on the min and max of the data
                #ax.set_ylim(df['Amplitude'].min(), df['Amplitude'].max())

                # Remove x-ticks for all but the last subplot
                if i < len(channel_names) - 1:
                    ax.set_xticklabels([])

            # Set common labels
            #axs[-1].set_xlabel('Time')


            ############################################################################
            # Constants
            pred_npts = 400  # Number of points in the window

            # Calculate start and end indices for the last 400 points
            start = max(0, len(stream[0].data) - pred_npts)
            end = len(stream[0].data)

            # Initialize arrays for the inset axes and patches for each channel
            inset_axes_list = [None for _ in range(3)]
            patches = [None for _ in range(3)]


            # Data for the current window
            current_window_data = np.array([stream[channel].data[start:end] for channel in range(3)]).astype('float64') 

            # Normalize the data: Z-score standardization
            for w in current_window_data:
                w -= np.mean(w)
                w /= np.std(w)
                w[np.isnan(w)] = 1e-5
                w[np.isinf(w)] = 1e-5
            print(np.max(current_window_data[0,:]), np.min(current_window_data[0,:]))
            # Compute the log Mel spectrograms and model predictions for the current window
            log_mel_spectrograms_stacked = compute_log_mel_spectrograms(torch.tensor(current_window_data).unsqueeze(0).detach().cpu().numpy())
            with torch.no_grad():
                pred_p, pred_s = model(torch.tensor(log_mel_spectrograms_stacked))
                pred = torch.cat((pred_p, pred_s), 0)

            # Plot model predictions
            axs[-1].clear()  # Clear the previous predictions
            axs[-1].set_title('P & S wave Probabilities')
            axs[-1].set_ylabel('Prediction Value')
            axs[-1].set_ylim(0, 1)  # Setting y-axis limits from 0 to 1
            axs[-1].grid(True)
            for j in range(pred.shape[0]):
                if j == 0:
                    axs[-1].plot(np.linspace(0, pred_npts, pred_npts), pred[j], label=f'P-wave')
                else:
                    axs[-1].plot(np.linspace(0, pred_npts, pred_npts), pred[j], label=f'S-wave')
            axs[-1].legend(loc='best')

            # Overlay the window and plot Mel spectrogram for each channel
            for j in range(3):
                ax = axs[j]
                
                # Create new inset for Mel spectrogram within the window bounds
                if inset_axes_list[j] is not None:
                    inset_axes_list[j].remove()
                inset_axes_list[j] = inset_axes(ax, width="100%", height="100%", bbox_to_anchor=(start, ax.get_ylim()[0], end - start, ax.get_ylim()[1] - ax.get_ylim()[0]), bbox_transform=ax.transData, borderpad=0)
                librosa.display.specshow(log_mel_spectrograms_stacked[0][j], sr=100, hop_length=20, ax=inset_axes_list[j], x_axis='time', y_axis='mel')
                inset_axes_list[j].axis('off')  # Hide the axis of the inset


            ##############################################################################


            # Adjust layout
            plt.tight_layout()  # Adjust as needed for the title and labels

            # Display the plot in Streamlit
            plot_placeholder_2.pyplot(fig)

            # Sleep for 1 seconds before rerunning the script
            #time.sleep(1)
            with col2:
                if torch.max(pred_p[0, 250:]) > 0.6 and not p_wave_detected:
                    text_placeholder.markdown('<p style="text-align: center;  font-weight: bold; font-size: 24px;">Status: P-wave detected! 📢</p>', unsafe_allow_html=True)
                    p_wave_detected = True
                    time.sleep(2)
                if torch.max(pred_s[0, 250:]) > 0.45 and not s_wave_detected:
                    s_wave_detected = True
                    text_placeholder.markdown('<p style="text-align: center;  font-weight: bold; font-size: 24px;">Status: S-wave detected! 📢</p>', unsafe_allow_html=True)
                    time.sleep(2)
                elif p_wave_detected and not s_wave_detected:
                    text_placeholder.markdown('<p style="text-align: center;  font-weight: bold; font-size: 24px;">Earthquake happening. S-wave is coming! ⚠️</p>', unsafe_allow_html=True)
                elif torch.max(pred_s) < 0.2  and torch.max(pred_p) < 0.2 :
                    text_placeholder.markdown('<p style="text-align: center;  font-weight: bold; font-size: 24px;">Status: All Clear 🟢</p>', unsafe_allow_html=True)