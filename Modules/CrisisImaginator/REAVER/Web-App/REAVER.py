import streamlit as st
import pandas as pd

# Display the main title
st.title('REAVER')

# Display a subtitle and introduction using Markdown for formatting
st.markdown("""

Predicting earthquakes with precision remains an ongoing challenge in **Earthquake Early Warning Systems (EEWS)**. These systems struggle with accuracy and often fail to provide timely warnings for impending earthquakes. Recent efforts employing deep learning techniques have shown promise in overcoming these limitations.

However, current methods lack the ability to capture subtle frequency changes indicative of seismic activity in real-time, limiting their effectiveness in EEWS.
""")

# Insert an image that represents the concept of REAVER
st.image('Arch_diagram_updated.png', caption='Real-time Earthquake Prediction with REAVER', use_column_width='auto')

# Continue with more detailed text
st.markdown("""
To address this gap, we propose **REAVER**, a novel approach for real-time prediction of P- and S-waves of earthquakes using attention-based sliding-window spectrograms. REAVER leverages Mel-Spectrogram signal representations to effectively capture temporal frequency changes in seismic signals. By employing an encoder-decoder architecture with attention mechanisms, REAVER accurately predicts the onset of P- and S-waves moments when an earthquake occurs.

**REAVER** is comprised of four key layers:

1. **Data Acquisition Layer**: This layer is responsible for gathering real-time and historical waveform data, ensuring a comprehensive dataset for analysis.
2. **Pre-processing Layer**: It segments the signal into overlapping windows and computes the Mel-Spectrogram for each window, preparing the data for further processing.
3. **Model Layer**: At this stage, REAVER predicts the continuous probabilities of P and S waves, utilizing the pre-processed data to make accurate forecasts.
4. **Warning Layer**: The final layer issues warnings to subscribers whenever the detection of P or S waves surpasses a predefined threshold, enabling immediate response actions.


### Key Features of REAVER:
- **Real-time Application**: Can be applied to continuous seismic waveforms to predict the onset of P and S waves in real-time.
- **Past Earthquake Analysis**: Enables users and seismoligsts to analyze past earthquake waveforms. 
- **Web-based Implementation**: Provides a user-friendly interface for monitoring seismic activity and analyzing historical earthquake waveforms.

### Benchmarking REAVER
We benchmark the effectiveness of REAVER, demonstrating its superior performance in terms of both accuracy and real-time prediction capabilities compared to existing methods.
""")

# Table 1: Performance comparison of P-wave detection time statistics
# Updated data including median, Q1, and Q3 values for each method
data_updated = {
    "Method": ["Phasenet", "Eqtransformer", "STA/LTA", "REAVER"],
    "Δt_mean (s)": [1.67, 3.73, 0.27, 0.08],
    "σ_Δt (s)": [2.01, 4.48, 0.31, 0.16],
    "Median (s)": [0.83, 1.62, 0.15, 0.04],
    "Q1 (s)": [0.59, 1.20, 0.04, 0.03],
    "Q3 (s)": [1.93, 4.00, 0.40, 0.12]
}

# Creating the updated DataFrame to reflect the new table structure
df_updated = pd.DataFrame(data_updated)


# Display Table 1 with a caption
st.markdown("### Performance Comparison of P-wave Detection Time Statistics")
st.table(df_updated)


# Write a sentence before displaying the confusion matrix
st.markdown("### Confusion Matrix for REAVER")
st.write("Below is the confusion matrix for REAVER, showcasing its performance in distinguishing between true positives, false positives, true negatives, and false negatives, with overall accurcy of **98.8%**.")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you've already imported pandas and streamlit as shown in previous examples

# REAVER model's confusion matrix data
reaver_metrics = {
    'True Positives': 50860,
    'False Negatives': 650,
    'True Negatives': 11671,
    'False Positives': 102,
    'Precision': 0.9979985086927514,
    'Recall': 0.9873810910502815,
    'F1 Score': 0.9926614099461315,
    'Overall Accuracy (%)': 98.81168718297172
}

# Function to plot confusion matrix
def plot_confusion_matrix(tp, fn, tn, fp):
    # Create a confusion matrix
    confusion_matrix = pd.DataFrame(
        [[tp, fn],
         [fp, tn]],
        columns=['Predicted Positive', 'Predicted Negative'],
        index=['Actual Positive', 'Actual Negative']
    )
    
    # Plot using seaborn for a nicer look
    plt.figure(figsize=(10, 7))
    sns.heatmap(confusion_matrix, annot=True, fmt="d", cmap="Blues", cbar=False, annot_kws={"size": 16})
    plt.title('Confusion Matrix for REAVER')
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    
    # Show plot in Streamlit
    st.pyplot(plt)

# Call the function with your data
plot_confusion_matrix(
    reaver_metrics['True Positives'],
    reaver_metrics['False Negatives'],
    reaver_metrics['True Negatives'],
    reaver_metrics['False Positives']
)
