import pandas as pd


"""
Interfaces
"""


class Tokenizer(object):
    def __init__(self, text_column):
        self.tokenizer = None
        self.text_column = text_column
        self.tokenized_text_column = 'tokenized_' + text_column

    def tokenize(self, pd_dataset):
        pass


class Lemmatizer(object):
    def __init__(self, text_column):
        self.lemmatizer = None

        self.tokenized_text_column = 'tokenized_' + text_column
        self.lemmatized_text_column = 'lemmatized_' + text_column

    def lemmatize(self, pd_dataset):
        pass


class Preprocessor(object):
    def __init__(self, text_column, remove_empty_rows=False):
        self.text_column = text_column
        self.tokenizer = Tokenizer(text_column)
        self.lemmatizer = Lemmatizer(text_column)

        self.tokenized_text_column = 'tokenized_' + text_column
        self.lemmatized_text_column = 'lemmatized_' + text_column

        self.remove_empty_rows = remove_empty_rows

    def pipeline(self, pd_dataset:pd.DataFrame) -> pd.DataFrame:
        pass