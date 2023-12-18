import stanza
from stanza.models.common.doc import Document
import traceback
import pandas as pd
import numpy as np
from tqdm import tqdm
import time

from preprocessing.Text_Prep.preprocessor.interface import Tokenizer, Lemmatizer


class StanzaBulkTokenizer(Tokenizer):
    def __init__(self, text_column, use_gpu=False, sentence_split=False):
        super().__init__(text_column)

        self.use_gpu = use_gpu
        self.package = "genia"
        self.processors = "tokenize"
        self.sentence_split = sentence_split

        stanza.download(lang="en", package=self.package,
                        processors=self.processors,
                        logging_level='WARN')

        self.pipeline = stanza.Pipeline(lang='en',
                        package=self.package, processors=self.processors,
                        use_gpu=self.use_gpu, logging_level='WARN')



    def tokenize_in_bulks(self, pd_dataset:pd.DataFrame, bulksize=1000):
        """
        Tokenize the dataframe in bulks using the stanza process_bulk mechanism.
        bulksize of 1000 seems to speed up the tokenization 3-4 times.

        :param pd_dataset:
        :param bulksize:
        :return:
        """

        print("\nTokenize in bulks")

        #Replace NaN rows with empty string as NaN causes errors during tokenization
        pd_dataset.replace(pd.NA, "", inplace=True)
        tok_text = []


        num_bulks = int(len(pd_dataset) / bulksize)
        pd_dataset[self.tokenized_text_column] = pd.NA

        for i in tqdm(range(num_bulks), leave=True, position=0):
            df_bulk = pd_dataset.iloc[i * bulksize:(i + 1) * bulksize, pd_dataset.columns.get_loc(self.text_column)]
            tokenized_bulk = self.tokenize_one_bulk(df_bulk)
            pd_dataset[i * bulksize:(i + 1) * bulksize][self.tokenized_text_column] = tokenized_bulk
            tok_text.extend(tokenized_bulk)

            if i%100==0:
                continue
                #self.reinitialize()

        # The remaining rows
        last_bulk = pd_dataset[num_bulks * bulksize:][self.text_column]
        if len(last_bulk) > 0:
            tokenized_last_bulk = self.tokenize_one_bulk(last_bulk)
            pd_dataset.iloc[num_bulks * bulksize:, pd_dataset.columns.get_loc(self.tokenized_text_column)] = tokenized_last_bulk
            tok_text.extend(tokenized_last_bulk)

        pd_dataset[self.tokenized_text_column] = tok_text

        return pd_dataset



    def tokenize_one_bulk(self, df_bulk):
        assert df_bulk.isna().sum() == 0, df_bulk[df_bulk.isna()]
        docs = []

        if isinstance(df_bulk, pd.DataFrame):
            for id, row in df_bulk.iterrows():
                docs.append(Document([], text=row))
        elif isinstance(df_bulk, pd.Series):
            for id, row in df_bulk.items():
                docs.append(Document([], text=row))
        else:
            raise ValueError(df_bulk, "not a pandas object")

        start_nlp = time.time()

        try:
            res = self.pipeline(docs)

        except Exception as e:
            '''
            print("\n")
            print(e)
            traceback.print_exc()
            print(df_bulk)
            print(docs)
            '''
            print("ERROR in stanza pipeline")
            tokenized_docs = []
            for doc in docs:
                try:

                    tokenized_doc = self.pipeline(doc)
                    tokenized_docs.append(tokenized_doc)
                except:
                    print("Skipping text tokenization for text:")
                    # print(doc, "\n")
                    tokenized_docs.append(np.nan)

            res = tokenized_docs

        #print("Stanza pipe in seconds:", time.time() - start_nlp)

        docs = []

        for doc in res:
            doc = doc.to_dict()
            report = []
            for sen in doc:
                if self.sentence_split:
                    sentence = []
                    for tok in sen:
                        sentence.append(tok["text"])
                    report.append(sentence)
                else:
                    for tok in sen:
                        report.append(tok["text"])

            docs.append(report)
            #docs.append([tok["text"] for sen in doc for tok in sen])


        return docs

    def reinitialize(self):
        """
        Initialize stanza from scratch

        :return:
        """

        self.pipeline = stanza.Pipeline(lang='en',
                                        package=self.package, processors=self.processors,
                                        use_gpu=self.use_gpu, logging_level='WARN')



class StanzaBulkLemmatizer(Lemmatizer):
    def __init__(self, text_column, use_gpu=False, sentence_split=False):
        super().__init__(text_column)
        self.use_gpu = use_gpu
        self.sentence_split = sentence_split

        stanza.download(lang="en", package='craft',
                        processors='tokenize,pos,lemma',
                        logging_level='WARN')

        self.pipeline = stanza.Pipeline(lang='en', package='craft',
                        processors='tokenize,lemma',
                        tokenize_pretokenized=True, #Set to True
                        use_gpu=self.use_gpu, logging_level='WARN')


    def lemmatize_in_bulks(self, pd_dataset, bulksize=1000):
        print("\nLemmatize in bulks")
        lemm_text = []

        # Replace NaN rows with empty string as NaN causes errors during tokenization
        pd_dataset.replace(pd.NA, "", inplace=True)

        pd_dataset[self.lemmatized_text_column] = pd.NA
        bulks = int(len(pd_dataset) / bulksize)

        for i in tqdm(range(bulks), leave=True, position=0):
            bulk = pd_dataset[i * bulksize:(i + 1) * bulksize][self.tokenized_text_column]
            lemmatized_bulk = self.lemmatize_one_bulk(bulk)
            #print(lemmatized_bulk[0])
            pd_dataset[i * bulksize:(i + 1) * bulksize][self.lemmatized_text_column] = lemmatized_bulk
            lemm_text.extend(lemmatized_bulk)

        # The remaining rows
        last_bulk = pd_dataset[bulks * bulksize:][self.tokenized_text_column]
        if len(last_bulk) > 0:
            last_bulk = self.lemmatize_one_bulk(last_bulk)
            pd_dataset[bulks * bulksize:][self.lemmatized_text_column] = last_bulk
            lemm_text.extend(last_bulk)

        #print(pd_dataset[self.lemmatized_text_column])
        pd_dataset[self.lemmatized_text_column] = lemm_text

        return pd_dataset


    def lemmatize_one_bulk(self, df_bulk):
        assert df_bulk.isna().sum() == 0
        docs = []

        if isinstance(df_bulk, pd.DataFrame):
            for id, row in df_bulk.iterrows():
                docs.append(Document([], text=[row]))
        elif isinstance(df_bulk, pd.Series):
            for id, row in df_bulk.items():
                if self.sentence_split:
                    pretokenized = []
                    for sen in row:
                        pretokenized += [tok for tok in sen] + ['\n']
                    pretokenized = " ".join(pretokenized)
                    docs.append(Document([], text=pretokenized))
                #[['tried', 'token', 'lemma']] -> "tried token lemma"
                #docs.append(Document([], text=[row]))
                else:
                     docs.append(Document([], text=" ".join(row)))

        else:
            raise ValueError(df_bulk, "not a pandas object")

        """Try lemmatization"""
        try:
            res = self.pipeline(docs)

        except Exception as e:

            print("ERRRRRRRRRRRRRRRORRRRRRRRRRRRRRRRR\n")
            print(e)
            traceback.print_exc()
            #print(df_bulk)
            #print(docs)
            #raise e


            lemmatized_docs = []
            for doc in docs:
                try:
                    #print(doc.text)
                    lemmatized_doc = self.pipeline(Document([], text=doc.text[0]))
                    #print(lemmatized_doc.text)
                    lemmatized_docs.append(lemmatized_doc)
                    #print(lemmatized_doc)
                    #print("\n\n")
                except Exception as e:
                    print("Skipping text lemmatization for text:")
                    # print(doc.text, "\n")
                    traceback.print_exc()
                    lemmatized_docs.append(np.nan)

            res = lemmatized_docs

        docs = []

        for doc in res:
            doc = doc.to_dict()
            report = []
            for sen in doc:
                if self.sentence_split:
                    sentence = []
                    for tok in sen:
                        sentence.append(tok["lemma"])
                    report.append(sentence)
                else:
                    for tok in sen:
                        report.append(tok["lemma"])

            docs.append(report)


        return docs
