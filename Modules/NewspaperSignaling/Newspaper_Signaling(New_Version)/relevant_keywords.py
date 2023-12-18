import pandas as pd

sentences_jan = pd.read_csv('dfmarch.txt', sep='\t')

from keyphrase_vectorizers import KeyphraseCountVectorizer
from keybert import KeyBERT
from flair.embeddings import TransformerDocumentEmbeddings

# Init German KeyBERT model
kw_model = KeyBERT(model=TransformerDocumentEmbeddings('dbmdz/bert-base-german-uncased'))

# Init vectorizer for the German language
vectorizer = KeyphraseCountVectorizer(spacy_pipeline='de_core_news_sm', pos_pattern='<ADJ.*>*<N.*>+', stop_words='german')
# use_maxsum=True, nr_candidates=20,
# Get German keyphrases
kw_model.extract_keywords(docs=sentences_jan, top_n=15, vectorizer=vectorizer)

