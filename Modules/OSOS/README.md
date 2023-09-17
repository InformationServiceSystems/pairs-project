# "Listening In": Social Signal Detection for Crisis Prediction

## 1. Description


<p> 

Crises send out early warning signals; mostly weak and difficult to detect amidst the noise of everyday life. These signals are readily available nowadays with the rise of social media, for instance, Twitter. A Major challenge in using tweets for crisis prediction is the handling of noise and irrelevant tweets. Most approaches tackle this challenge by applying natural language processing techniques, such as sentiment analyses, and content analyses, showing disadvantages due to the limited scope of
training data and thus, low performance in terms of accuracy (high percentage of False Positives). We present OSOS – a method for open-domain social signal detection of crisis-related indicators in tweets. Our method works with multi-lingual Twitter data and combines multiple state-of-the-art models for data pre-processing and data filtration. It supports most of the spoken languages in the world. The method can detect social signals in tweets for open domains, e.g., energy, finances, and supply chains, that can be directly adjusted by the user in terms of keywords and crisis data obtained by Twitter.**
    
</p>


## 2. Approach

<p> 

We present OSOS – a method for open-domain social signal detection of crisis-related indicators in tweets. Our method consists of three main steps to perform the task of social signal detection for crisis prediction Data Pre-processing, Data Filtration, and Signal Detector. OSOS operates on unstructured multi-lingual data obtained by Twitter as well as domain-specific keywords given by a user and configuration parameters such as preferred country and time interval.
This serves as input for the Data Pre-processing which handles data cleaning including the removal of stopwords, punctuations, and duplicates as well as
performs tokenization and sentence parsing. Resulting data are fed into the Data Filtration step which performs extensive filtering of tweets using a state-of-the-art GPT-3 model for text classification and DistilBERT for sentiment analyses. Outputs of this step are transferred to the Signal Detector which is charged with trend
analyses using burst detection. That means the frequency of relevant tweets is monitored and time series with exponential growth in frequency are identified to find possible burst periods.

<p> 

!["Demo"](Images/Methodology.png)

## 4. Installation 

- Prerequisites:

	```Python 3.9 or higher.``` You can follow [this guide](https://phoenixnap.com/kb/upgrade-python) on how to install it on Windows/macOS/Linux.

- Clone/Download the repository:

	- Open a terminal (Linux) or cmd (Windows) and run the following command to clone the repository:
	```
	git clone https://github.com/InformationServiceSystems/pairs-project.git
	```

- Install the dependencies 

	- In the terminal, run the following command to go to OSOS directory. 
	```
	cd pairs-project/Modules/OSOS/
	```
	- Then run this command to install the dependencies
	```
	pip install -r requirements.txt
	```

- Run the Python file Full_Pipeline.py


