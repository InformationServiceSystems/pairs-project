import pandas as pd
import stanza
from nltk.corpus import stopwords
import string
import re
import sys

from preprocessing.Text_Prep.preprocessor.regular_expressions import RegularExpressions
from preprocessing.Text_Prep.preprocessor.interface import Preprocessor

class TextPreprocessor(Preprocessor):

    def __init__(self, text_column:str, remove_empty_rows=False):
        super(TextPreprocessor, self).__init__(text_column=text_column, remove_empty_rows=remove_empty_rows)

        stanza.download('de', package='genia', processors='tokenize',
                        logging_level='WARN')
        stanza.download(lang="de", package='craft', processors='tokenize,pos,lemma',
                        logging_level='WARN')

        self.additional_stop_words = ["'s"]
        self.stopwords = stopwords.words('german') + self.additional_stop_words
        self.RE = RegularExpressions()


    def shorten_char_repetitions(self, text):
        return self.RE.shorten_char_repetitions(text)

    def uniformize_units(self, text):
        return self.RE.uniformize_units(text)

    def clean(self, text):
        clean_text = []
        for tok in text:
            if tok not in self.stopwords and tok not in string.punctuation:
                # remove tokens of length 1 if not a digit
                if len(tok) > 1 or tok.isdigit():
                    clean_text.append(tok)
        return clean_text

    def remove_whitespaces_in_regular_expressions(self, tokenized_text):
        sent_str = " ".join(tokenized_text)
        for token in self.RE.tokens:
            matches = re.findall(self.RE.tokens[token], sent_str)
            for match in matches:
                match_phrase = match.replace(' ', '')
                sent_str = sent_str.replace(match, ' '+match_phrase+' ')
        return sent_str.split()

    # splitting at punctuation that the stanza tokenizer missed
    def split_tokens(self, tokenized_text):
        sent_str = " ".join(tokenized_text)
        previous_sent_str = sent_str
        punct = ['“', '"', '’', '`', '´', "”", "'", '‘', ',', '.', '=', ':', ';', '*', '≥','≤', '<', '>', '~', '−', '-',
                 '+', '#', '[', ']', '(', ')', '{', '}', '\\', '/', '?', '!', '±']
        while True:
            for tok in sent_str.split():
                # trailing punctuation split off
                if tok[-1] in punct and len(tok) > 1:
                    new_tok = tok[:-1]+' '+tok[-1]
                    sent_str = sent_str.replace(tok, new_tok)
                    tok = new_tok
                # punctuation at beginning of token split
                if tok[0] in punct and len(tok) > 1:
                    new_tok = tok[0]+' '+tok[1:]
                    sent_str = sent_str.replace(tok, new_tok)
                    tok = new_tok
                # split alternatives with slash
                if "/" in tok and not RegularExpressions().is_unit(tok) and tok not in RegularExpressions().tokens and len(tok) > 1:
                    split_tok = tok.split('/')
                    new_tok = " / ".join(split_tok)
                    sent_str = sent_str.replace(tok, new_tok)
            if sent_str == previous_sent_str:
                break
            else:
                previous_sent_str = sent_str
        return sent_str.split()


    def delete_empty_rows(self, pd_dataset:pd.DataFrame, text_column:str):
        if len(pd_dataset[pd_dataset[text_column] == '']) > 0:
            print(f"Empty rows to be removed:\n{pd_dataset[pd_dataset[text_column] == '']}")
            pd_dataset = pd_dataset[pd_dataset[text_column] != ""]
            pd_dataset.reset_index(drop=True, inplace=True)

        return pd_dataset
