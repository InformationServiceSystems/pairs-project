import pandas as pd
from bs4 import BeautifulSoup
from dateparser import parse as parse_date
from urllib.request import urlopen

count = 0

def get_content(link, para_length=3):
    total_paragraph_to_extract = para_length
    global count
    content = ''
    try:
        soup = BeautifulSoup(urlopen(link), 'html.parser')
        pages = soup.find_all('p')
        for idx in range(0, min(total_paragraph_to_extract, len(pages))):
            content = content + ' ' + pages[idx].getText().strip()
    except:
        count += 1
    
    return content


def get_articles_content(news_article_df, para_length=3):
    news_article_df['text'] = news_article_df['link'].apply(get_content, para_length=para_length)
    print('Total news articles: {}'.format(len(news_article_df)))
    print('Total articles with sucessful content: {}'.format(len(news_article_df)-count))
    print('total articles with failure count', count)

    # when the content is not available, then put the title as content
    news_article_df['text'] = news_article_df['text'].apply(lambda x: x if x != '' else news_article_df['title'])

    return news_article_df


if __name__ == "__main__":
    news_article_df = pd.read_csv("1_goggle_news.csv")
    news_article_df = get_articles_content(news_article_df)
    news_article_df.to_csv('2_goggle_news_paragraph.csv')