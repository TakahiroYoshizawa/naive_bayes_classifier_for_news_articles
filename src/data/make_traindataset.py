# -*- coding: utf-8 -*-
import os
import click
import logging
import urllib.request as urlreq
from bs4 import BeautifulSoup
import ssl
import MeCab
import pandas as pd
import time
import numpy as np
import re


def Get_Url_List():
    """
    #カテゴリ別ランキングページ上位１０ページまでに載っている記事のURLをカテゴリごとにまとめてCSV格納
    :return: url_dict
    """

    ssl._create_default_https_context = ssl._create_unverified_context

    url_dict = pd.DataFrame()

    for i in range(1, 9):
        url_list = []

        for j in range(1, 11):
            time.sleep(1)
            url_to_open = 'https://gunosy.com/categories/' + str(i) + '/ranking?page=' + str(j)
            html = urlreq.urlopen(url_to_open)
            soup = BeautifulSoup(html, 'html.parser')
            gunocy_main_bsobj = BeautifulSoup(str(soup.find_all('div', 'list_thumb')), 'html.parser')

            for a_tag in gunocy_main_bsobj.findAll("a"):
                url_list.append(str(a_tag.get('href')))

        url_list = pd.Series(url_list, name='catg'+str(i))
        url_dict = pd.concat([url_dict, url_list], axis=1)

    url_dict.to_csv("Gunosy_urllist_0814.csv", encoding='utf-8')

    print(url_dict)

    return url_dict


def URLDict_to_WordsVector(url_dict):





def Get_TitleArticle(url):
    '''
    記事のURLを入力すると，その記事のタイトルと記事本文が出力される関数
    :argument url
    :return: Title, Article
    '''
    ssl._create_default_https_context = ssl._create_unverified_context
    html = urlreq.urlopen(url).read()

    soup = BeautifulSoup(html, "lxml")
    title_part = soup.find_all("h1", {"class": "article_header_title"})
    article_part = soup.find_all("div", {"class": "article gtm-click"})

    title = title_part[0].get_text()
    article = article_part[0].get_text()

    time.sleep(1)

    return url, title, article


def Keitaiso_Kaiseki(title, article):
    """
    
    :param title: 
    :param article: 
    :return: 
    """

    print(title)
    print(article)

    # TODO: MeCab.Tagger()でRuntimeErrorを解消しなきゃいけない.
    # うまく行った
    # bash $ brew install mecab-ipadic
    m = MeCab.Tagger()
    article = m.parse(article)

    print(article.split('\n'))

    article_list = [word.split('\t') for word in article.split('\n')]

    del article_list[-1]
    del article_list[-1]

    article_df = pd.DataFrame(article_list, columns=['word', 'word_class'])
    article_df['word_class'] = article_df['word_class'].str.split(',')
    article_df['word_class'] = article_df['word_class'].apply(lambda x: x[0])

    article_df_noun = article_df[article_df['word_class' == '名詞']]
    print(article_df_noun.groupby('word').count().sort_values('word_class', ascending=False))


def main():
    """ 
    Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    """
    # logger = logging.getLogger(__name__)
    # logger.info('making final data set from raw data')

    url_dict = Get_Url_List()
    # url, title, article = Get_TitleArticle()
    # keitaiso_kaiseki(title, article)


if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    # project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    # load_dotenv(find_dotenv())

    main()
