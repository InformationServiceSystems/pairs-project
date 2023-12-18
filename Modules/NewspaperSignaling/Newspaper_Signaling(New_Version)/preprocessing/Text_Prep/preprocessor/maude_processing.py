import re
import os
import pandas as pd
from tqdm import tqdm
import numpy as np


from preprocessing.Text_Prep.preprocessor.text_preprocessing import TextPreprocessor
from preprocessing.Text_Prep.preprocessor.interface import Preprocessor
from preprocessing.Text_Prep.preprocessor.stanza_bulk_processing import StanzaBulkTokenizer, StanzaBulkLemmatizer

class MaudePreprocessor(TextPreprocessor):

    def __init__(self, pd_data=pd.DataFrame()):
        super().__init__(text_column="text")

        self.data = pd_data


    # makes all lowercase, replaces spanish question mark and shorten char repetitions
    def pre_tokenization_processing(self, text_column):
        #self.data['tokenized_text'] = [[] for i in range(len(self.data))]
        print("\nPre-tokenization processing")
        for idx, text in tqdm(self.data[text_column].items(), total=len(self.data)):
            if text is not None:
                text = text.lower()
                text = self.remove_spanish_questionmark(text)
                text = super().shorten_char_repetitions(text)
                self.data.at[idx, text_column] = text


    def remove_spanish_questionmark(self, text):
        whitespace_tok = text.split()
        tok_list = []
        for tok in whitespace_tok:
            match = re.search(r'[A-Za-z]+¿s', tok)
            if match:
                tok = tok.replace('¿', "'")
            else:
                tok = tok.replace('¿', '')
            tok_list.append(tok)
        text = " ".join(tok_list)
        return text


    def post_tokenization_correction(self, text_column:str="tokenized_text"):
        print("\nTokenizer post-corrections")
        for idx, tokenized_text in tqdm(self.data[text_column].items(), total=len(self.data)):
            if all(isinstance(l, list) for l in tokenized_text):
                tokenized_sentences = []
                for sent in tokenized_text:
                    tokenized_sent = super().split_tokens(sent)
                    tokenized_sent = super().remove_whitespaces_in_regular_expressions(tokenized_sent)
                    tokenized_sent = super().uniformize_units(" ".join(tokenized_sent))
                    tokenized_sentences.append(tokenized_sent)
                self.data.at[idx, text_column] = tokenized_sentences
            else:
                tokenized_text = super().split_tokens(tokenized_text)
                tokenized_text = super().remove_whitespaces_in_regular_expressions(tokenized_text)
                tokenized_text = super().uniformize_units(" ".join(tokenized_text))
                self.data.at[idx, text_column] = tokenized_text
            if len(tokenized_text) == 0:
                continue
        return self.data



    # removing unwanted tokens after tokenization/lemmatization
    def clean(self, text_column:str="lemmatized_text"):
        print("\nFinal Cleaning")
        for idx, text in tqdm(self.data[text_column].items(), total=len(self.data)):
            if not text is None:
                if all(isinstance(l, list) for l in text):
                    cleaned_text = []
                    for sent in text:
                        cleaned_text.append(super().clean(sent))
                    self.data.at[idx, text_column] = cleaned_text
                else:
                    self.data.at[idx, text_column] = super().clean(text)


    def remove_whitespaces_in_regular_expressions(self, sent_str):
        for token in self.regular_expressions:
            matches = re.findall(self.regular_expressions[token], sent_str)
            for match in matches:
                match_phrase = match.replace(' ', '')
                sent_str = sent_str.replace(match, ' '+match_phrase+' ')
        return sent_str


    # all post-tokenization correction steps
    def post_token_corrections(self, seg_text):
        sent_str = " ".join(seg_text)
        sent_str = self.remove_whitespaces_in_regular_expressions(sent_str)
        sent_str = super().uniformize_units(sent_str)
        sent_str = super().split_tokens(sent_str)
        if len(sent_str) > 0:
            return sent_str
        else:
            return np.nan


class MaudeBulkPreprocessor(Preprocessor):
    def __init__(self, use_gpu=False, sentence_split=False):
        super().__init__(text_column="text")
        self.tokenizer = StanzaBulkTokenizer(use_gpu=use_gpu, text_column="text", sentence_split=sentence_split)
        self.lemmatizer = StanzaBulkLemmatizer(use_gpu=use_gpu, text_column="text", sentence_split=sentence_split)

        self.preprocessor = MaudePreprocessor()

    def pipeline(self, pd_dataset, text_column="text"):
        self.preprocessor.data = pd_dataset
        pd_dataset.dropna(subset=["text"], inplace=True)

        # cleaning before tokenization
        self.preprocessor.pre_tokenization_processing(text_column)

        # tokenize with standard stanza in bulks
        temp_df = self.tokenizer.tokenize_in_bulks(self.preprocessor.data, bulksize=500)

        temp_df = temp_df.dropna(subset=['tokenized_text'])
        temp_df.reset_index(inplace=True, drop=True)
        self.preprocessor.data = temp_df

        # manually correct tokens
        temp_df = self.preprocessor.post_tokenization_correction()
        # lemmatize with stanza (pretokenized) in bulks
        temp_df = self.lemmatizer.lemmatize_in_bulks(temp_df, bulksize=100)
        # 'final' preprocessing results is now stored under "lemmatized_text" !!!
        self.preprocessor.clean()

        self.preprocessor.data.dropna(subset=['lemmatized_text'], inplace=True)
        self.preprocessor.data.reset_index(inplace=True, drop=True)

        return self.preprocessor.data


if __name__ == "__main__":
    pd.set_option('display.max_columns', 95)
    pd.set_option('display.width', 500000)
    pd.set_option('display.max_rows', 70)
    pd.set_option('display.max_colwidth', 200)

    T = MaudeBulkPreprocessor( sentence_split=False)

    ftr_name = os.path.join(SMPaths.MAUDE_FOLDER, "100000_random_entries_prod_codes.ftr")
    ftr = load_feather(ftr_name)
    maude = MaudePDDataset(ftr).get_all_report_texts()[:50000]

    prep_maude = T.pipeline(maude, 'text')

    exit(99)

    savepath = os.path.join(SMPaths.MAUDE_FOLDER, "20000_tokenized_entries.ftr")
    maude.to_feather(savepath)


    ftr_name = os.path.join(SMPaths.MAUDE_FOLDER, "20000_tokenized_entries.ftr")
    ftr = load_feather(ftr_name)


    data = MaudePDDataset(ftr).data
    Vocab = BuildVocabulary(data, 'lemmatized_text')
    Vocab.build_vocab()
    Vocab.compute_OOV_and_vocab()
    Vocab.save_vocabs(vocab_savepath=os.path.join(SMPaths.ROOT_PATH, "data", "vocab", "maude_vocab.txt"),
                      oov_savepath=os.path.join(SMPaths.ROOT_PATH, "data", "vocab", "maude_OOV_vocab.txt"),
                      valid_vocab_savepath=os.path.join(SMPaths.ROOT_PATH, "data", "vocab", "maude_valid_vocab.txt"))

    exit(99)
