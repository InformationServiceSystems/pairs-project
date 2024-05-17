# REAVER

We propose **REAVER**, a novel approach for real-time prediction of P- and S-waves of earthquakes using attention-based sliding-window spectrograms. REAVER leverages Mel-Spectrogram signal representations to effectively capture temporal frequency changes in seismic signals. By employing an encoder-decoder architecture with attention mechanisms, REAVER accurately predicts the onset of P- and S-waves moments when an earthquake occurs.



![gif](./video2.gif)


**REAVER** is comprised of four key layers:

1. **Data Acquisition Layer**: This layer is responsible for gathering real-time and historical waveform data, ensuring a comprehensive dataset for analysis.
2. **Pre-processing Layer**: It segments the signal into overlapping windows and computes the Mel-Spectrogram for each window, preparing the data for further processing.
3. **Model Layer**: At this stage, REAVER predicts the continuous probabilities of P and S waves, utilizing the pre-processed data to make accurate forecasts.
4. **Warning Layer**: The final layer issues warnings to subscribers whenever the detection of P or S waves surpasses a predefined threshold, enabling immediate response actions.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or newer installed on your system.
- Necessary Python packages installed. You can install the required packages using the `requirements.txt` file provided in the project directory.

### Installation

1. Clone the repository or download the ZIP package and extract it.
2. Navigate to the project directory and install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Ensure you have Streamlit installed, as it is necessary for running the web application.


## Running the Web Application

To run the web application:


1. Download the checkpoint file from (https://drive.google.com/file/d/16VFvXVnbQh6B3ANVbX_XQHSgeBcvSd3q/view?usp=sharing)
2. Add the checkpoint file to the directory REAVER/REAVER/model_checkpoints
3. Navigate to the `Web-App` directory within the project folder.

```bash
cd Web-App
```

4. Start the web application using Streamlit:

```bash
streamlit run REAVER.py
```

3. Open a web browser and go to the address provided by Streamlit to access the web application.

## Training the Model

To train the model, follow these steps:

1. Navigate to the `REAVER` directory within the project folder.
2. Run the training script:

```bash
python3 train.py
```