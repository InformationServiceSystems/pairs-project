import datetime
import pandas as pd

from googlenewsapi import get_news
from news_articles_paragraph import get_articles_content
from tok_lem_pipeline import tokenize_whole_maude

from roberta_classification import RobertaClassification
roberta_obj = RobertaClassification()

def google_news_extractor():
    query = "Energieknappheit" and "Ölkrise" and "Gaskrise" and "Stromkrise" and "fossile brennstoffe" and "kernenergie"\
            and "Kohlenstoffemissionen" and "Stromausfall" and "Stromunterbrechung" and "Brennstoff" and "Gaspreis" and "Strom" \
            and "Stromkosten" and "Energie" and "Kohle" and "Stromnachfrage" and "Energieerzeugung" and "Energieversorgung" \
            and "Gaskosten" and "Energiekrise" and "Solarenergie" and "Windenergie" and "Wasserkraft" and "Geothermie" and "Biomasseenergie" \
            and "erdöl" and "erdgas" 
    country = 'Germany'
    language = 'de'
    start_date = datetime.date(2022,12,1)
    end_date = datetime.date(2022,12,3)
    delta = datetime.timedelta(days=1)

    news_articles = get_news(query, start_date=start_date, end_date=end_date, country=country, language=language)
    print('Total news extracted: {}'.format(len(news_articles)))
    df = pd.DataFrame(news_articles)
    print(df)
    return df

def news_articles_paragraph_extractor(news_article_df):
    news_article_df = get_articles_content(news_article_df, para_length=3)
    print('Total news articles: {}'.format(len(news_article_df)))
    print(news_article_df.columns)
    print(news_article_df)
    return news_article_df

def data_processing(news_article_df):
    data = tokenize_whole_maude(news_article_df)
    return data

def keyword_filter(news_article_df, main_keyword):
    categories_to_clasify = [main_keyword, "Others"]
    threshold = 0.80
    text_column = "text"

    # loop over dataframe and classify each row
    for index, row in news_article_df.iterrows():
        confidence_scores = roberta_obj.roberta_classifier(row[text_column], categories_to_clasify, threshold, text_column)
        if confidence_scores[main_keyword] < threshold:
            news_article_df.drop(index, inplace=True)

    return news_article_df

def tense_filter(news_article_df):
    categories_to_clasify = ['past', 'present', 'future']
    threshold = 0.70
    text_column = "text"

    # loop over dataframe and classify each row
    for index, row in news_article_df.iterrows():
        confidence_scores = roberta_obj.roberta_classifier(row[text_column], categories_to_clasify, threshold, text_column)
        if (confidence_scores['present'] + confidence_scores['future']) < threshold:
            news_article_df.drop(index, inplace=True)

    return news_article_df

def alert_keyword_filter(news_article_df, alert_keyword):
    categories_to_clasify = [alert_keyword, 'Others']
    threshold = 0.70
    text_column = "text"

    # loop over dataframe and classify each row
    for index, row in news_article_df.iterrows():
        confidence_scores = roberta_obj.roberta_classifier(row[text_column], categories_to_clasify, threshold, text_column)
        if confidence_scores[alert_keyword] < threshold:
            news_article_df.drop(index, inplace=True)

    return news_article_df

def alert_level_filter(news_article_df):
    categories_to_clasify = ['high alert', 'low alert', 'others']
    threshold = 0.70
    text_column = "text"


    # loop over dataframe and classify each row
    for index, row in news_article_df.iterrows():
        confidence_scores = roberta_obj.roberta_classifier(row[text_column], categories_to_clasify, threshold, text_column)

        # find the key with the highest value
        alert_class = max(confidence_scores, key=confidence_scores.get)
        alert_score = confidence_scores[alert_class]

        news_article_df.at[index, 'alert_class'] = alert_class
        news_article_df.at[index, 'alert_score'] = alert_score

    return news_article_df


def alert_system(news_article_df):
    alert_dict = {}

    # get total length of news_article_df
    total_news = len(news_article_df)
    print('Total news: {}'.format(total_news))

    # total articles with alert_class = high alert
    high_alert = len(news_article_df[news_article_df['alert_class'] == 'high alert'])
    print('High alert: {}'.format(high_alert))

    # total articles with alert_class = low alert
    low_alert = len(news_article_df[news_article_df['alert_class'] == 'low alert'])
    print('Low alert: {}'.format(low_alert))

    # total articles with alert_class = others
    others = len(news_article_df[news_article_df['alert_class'] == 'others'])
    print('Others: {}'.format(others))

    # return the column text and alert_score for high alert articles with max and second max alert_score
    high_alert_df = news_article_df[news_article_df['alert_class'] == 'high alert']
    high_alert_df = high_alert_df.sort_values(by=['alert_score'], ascending=False)
    high_alert_df = high_alert_df[['text', 'alert_score']]
    high_alert_df = high_alert_df.reset_index(drop=True)

    # add to dictionary
    alert_dict['Total news'] = total_news
    alert_dict['High alert'] = high_alert
    alert_dict['Low alert'] = low_alert
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


    return alert_dict

   



if __name__ == "__main__":
    main_keyword = 'Energy crisis'
    alert_keyword = 'Energy price'
    # google newsapi
    news_article_df = google_news_extractor()
    # news_article_df.to_csv('1_goggle_news.csv')

    # news_article_df = pd.read_csv("1_goggle_news.csv")

    # news articles paragraph
    news_article_df = news_articles_paragraph_extractor(news_article_df)
    # news_article_df.to_csv('2_goggle_news_paragraph.csv')

    # news_article_df = pd.read_csv("2_goggle_news_paragraph.csv", encoding='utf-8', encoding_errors='ignore')
    news_article_df = data_processing(news_article_df)
    # news_article_df.to_csv('3_goggle_news_paragraph_lemmatized.csv')

    # news_article_df = pd.read_csv("3_goggle_news_paragraph_lemmatized.csv", encoding='utf-8', encoding_errors='ignore')


    # 2-stage filtration
    news_article_df = keyword_filter(news_article_df, main_keyword) 
    news_article_df = tense_filter(news_article_df)
    
    # alert analysis
    news_article_df = alert_keyword_filter(news_article_df, alert_keyword)
    news_article_df = alert_level_filter(news_article_df)

    # alert system
    alert_results = alert_system(news_article_df)
    print(alert_results)






