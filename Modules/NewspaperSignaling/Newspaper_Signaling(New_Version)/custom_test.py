# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 10:27:04 2023

@author: monse
"""
import datetime
import pandas as pd

from openai import OpenAI
import re
#%%
from googlenewsapi import get_news
from news_articles_paragraph import get_articles_content
from tok_lem_pipeline import tokenize_whole_maude
#%%
from roberta_classification import RobertaClassification

#%%
# Get user input for search query
query = input("Enter your search query: ")

# Get user input for start date
start_date_str = input("Enter the start date (YYYY-MM-DD): ")
try:
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD format.")
    exit()

# Get user input for end date
end_date_str = input("Enter the end date (YYYY-MM-DD): ")
try:
    end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date()
except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD format.")
    exit()

# Get user input for country and language
country = input("Enter the country (e.g., Germany): ")
language = input("Enter the language (e.g., de): ")

# Call the get_news function with user input
result = get_news(query, start_date, end_date, country, language)
print('Total news extracted: {}'.format(len(result)))
df_new = pd.DataFrame(result)

#%%
news_article_df = get_articles_content(df_new, para_length=1)
print('Total news articles: {}'.format(len(news_article_df)))
print(news_article_df.columns)


#%%
data = tokenize_whole_maude(news_article_df)
#print(news_article_df)
#%%
"""
import nltk
nltk.download('wordnet')
#%%
from nltk.corpus import wordnet

def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return synonyms

sy = get_synonyms(query)

#%%

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key='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',
)

new_query = "Find synonyms or related keywords for '" + query + "'"

# Make the API call
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": query}
    ],
    n=1,
    max_tokens=1024,
    temperature=0.5,
)

# Extract the generated text
generated_text = response.choices[0].message.content
#%%
# Split the generated text into words
w = generated_text.split()

# Create a set to store the unique keywords
keywords = set(w)
#%%

with open('german_stopwords_full.txt', 'r') as f:
    german_stopwords = set(f.read().splitlines())
g_stop_words = german_stopwords

e_stop_words = {"the", "and", "of", "to", "in", "that", "is", "with", "for", "on"}
#%%

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def calculate_cosine_similarity(query, words):
    # Combine query and words to create a list of all tokens
    all_tokens = [query] + list(words)

    # Convert the list of tokens to a TF-IDF matrix
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_tokens)

    # Calculate cosine similarity between the query and each word
    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])

    # Extract similarity scores and create a list of lists
    result = [[word, score] for word, score in zip(words, similarity_scores[0])]

    return result

similar_words = calculate_cosine_similarity(query, w)
#%%

# Add each word to the set if it's not a stop word

for word in words:
    if language == 'de':
        if word.lower() not in g_stop_words:
            keywords.add(word.lower())
    else:
        if word.lower() not in e_stop_words:
            keywords.add(word.lower())
        

# Convert the set of keywords to a list
keywords = list(keywords)

#%%
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Combine the keywords and article texts
texts = keywords + news_article_df['text'].tolist()

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(texts)

# Compute cosine similarity between each article and the keywords
similarity_scores = cosine_similarity(tfidf_matrix[len(keywords):], tfidf_matrix[:len(keywords)])

# Compute the mean similarity score for each article
mean_scores = np.mean(similarity_scores, axis=1)

# Set your threshold
threshold = 0.0001  # replace with your threshold

# Discard articles with a mean similarity score below the threshold
news_article_df = news_article_df[mean_scores >= threshold]
#%%

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Assume 'query_word' is the query word you want to compare with
query_word = query

texts = news_article_df['tokenized_text'].tolist()

# Calculate cosine similarity for each document
max_similarity_scores = []
for words in texts:
    # Join the tokenized words into a single string for each document
    document_text = ' '.join(words + [query_word])

    # Vectorize the document
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([document_text, query_word])

    # Compute cosine similarity
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    
    # Append the maximum similarity score to the list
    max_similarity_scores.append(np.max(similarity))

# Add the maximum similarity scores to the dataframe
news_article_df['query_max_similarity_score'] = max_similarity_scores

# Add the similarity scores to the dataframe
#ews_article_df['query_similarity_score'] = query_similarity_scores

# Set your threshold
#threshold = 0.0001  # replace with your threshold

# Discard articles with a similarity score below the threshold
#news_article_df = news_article_df[news_article_df['query_similarity_score'] >= threshold]



#%%
roberta_obj = RobertaClassification()
#main_keyword = "Gas"
"""
#%%
categories_to_clasify = ['past', 'present', 'future']
threshold = 0.50
text_column = "text"

# loop over dataframe and classify each row
for index, row in news_article_df.iterrows():
    confidence_scores = roberta_obj.roberta_classifier(row[text_column], categories_to_clasify, threshold)
    if (confidence_scores['present'] + confidence_scores['future']) < threshold:
        news_article_df.drop(index, inplace=True)

#%%
categories_to_clasify = ['Risk and Warning', 'Caution and Advice', 'Safe and Harmless']
threshold = 0.50
text_column = "text"


# loop over dataframe and classify each row
for index, row in news_article_df.iterrows():
    confidence_scores = roberta_obj.roberta_classifier(row[text_column], categories_to_clasify, threshold)
    # find the key with the highest value
    alert_class = max(confidence_scores, key=confidence_scores.get)
    alert_score = confidence_scores[alert_class]

    news_article_df.at[index, 'alert_class'] = alert_class
    news_article_df.at[index, 'alert_score'] = alert_score



categories_to_clasify = ['Risk and Warning', 'Caution and Advice', 'Safe and Harmless']
threshold = 0.70
text_column = "text"


# loop over dataframe and classify each row
for index, row in news_article_df.iterrows():
    confidence_scores = roberta_obj.roberta_classifier(row[text_column], categories_to_clasify, threshold)

    # find the key with the highest value
    alert_class = max(confidence_scores, key=confidence_scores.get)
    alert_score = confidence_scores[alert_class]

    news_article_df.at[index, 'alert_class'] = alert_class
    news_article_df.at[index, 'alert_score'] = alert_score

#%%
alert_dict = {}

# get total length of news_df
total_news = len(news_article_df)
print('Total news: {}'.format(total_news))

# total articles with alert_class = high alert
high_alert = len(news_article_df[news_article_df['alert_class'] == 'Risk and Warning'])
print('Risk and Warning: {}'.format(high_alert))

# total articles with alert_class = low alert
low_alert = len(news_article_df[news_article_df['alert_class'] == 'Caution and Advice'])
print('Caution and Advice: {}'.format(low_alert))

# total articles with alert_class = others
others = len(news_article_df[news_article_df['alert_class'] == 'Safe and Harmless'])
print('Safe and Harmless: {}'.format(others))

# return the column text and alert_score for high alert articles with max and second max alert_score
high_alert_df = news_article_df[news_article_df['alert_class'] == 'Risk and Warning']
high_alert_df = high_alert_df.sort_values(by=['alert_score'], ascending=False)
high_alert_df = high_alert_df[['text', 'alert_score']]
high_alert_df = high_alert_df.reset_index(drop=True)

# add to dictionary
alert_dict['Total news'] = total_news
alert_dict['Risk and Warning'] = high_alert
alert_dict['Caution and Advice'] = low_alert
alert_dict['Others'] = others

if len(high_alert_df) == 0:
    alert_dict['First high alert text'] = None
    alert_dict['First high alert score'] = None
    alert_dict['Second high alert text'] = None
    alert_dict['Second high alert score'] = None
elif len(high_alert_df) == 1:
    alert_dict['First high alert text'] = high_alert_df['text'][0]
    alert_dict['First high alert score'] = high_alert_df['alert_score'][0]
    alert_dict['Second high alert text'] = None
    alert_dict['Second high alert score'] = None
else: # len(high_alert_df) > 1
    alert_dict['First high alert text'] = high_alert_df['text'][0]
    alert_dict['First high alert score'] = high_alert_df['alert_score'][0]
    alert_dict['Second high alert text'] = high_alert_df['text'][1]
    alert_dict['Second high alert score'] = high_alert_df['alert_score'][1]
#%%
# Process the result as needed
# for item in result:
#     print(f"Title: {item['title']}")
#     print(f"Link: {item['link']}")
#     print(f"Published: {item['published']}")
#     print("--------")
#%%
import pickle
with open('alert_dict.pkl', 'wb') as f:
    pickle.dump(new_dict, f)

#%%

start_date_str = input("Enter the start date (YYYY-MM-DD): ")
try:
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD format.")
    exit()
print(start_date.month)
