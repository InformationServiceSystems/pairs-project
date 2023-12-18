"""
Pipelines to prepare, tokenize and lemmatize different dataset for ML
"""
import pandas as pd

from preprocessing.Text_Prep.preprocessor.maude_processing import MaudeBulkPreprocessor



def tokenize_whole_maude(data_df):

    maude_bulk_pre = MaudeBulkPreprocessor()

    prep_maude = maude_bulk_pre.pipeline(pd_dataset=data_df)

    prep_maude.to_csv("Lemmatised11-22.csv", sep=",")
    return prep_maude



if __name__ == "__main__":

    tokenize_whole_maude()


