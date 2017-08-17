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

        for j in range(1, 10):
            time.sleep(1)
            url_to_open = 'https://gunosy.com/categories/' + str(i) + '/ranking?page=' + str(j)

            html = urlreq.urlopen(url_to_open)
            soup = BeautifulSoup(html, 'html.parser')
            gunocy_main_bsobj = BeautifulSoup(str(soup.find_all('div', 'list_thumb')), 'html.parser')

            for a_tag in gunocy_main_bsobj.findAll("a"):
                url_list.append(str(a_tag.get('href')))

        url_list = pd.Series(url_list, name='catg'+str(i))
        url_dict = pd.concat([url_dict, url_list], axis=1)

    url_dict.to_csv("Gunosy_urllist_0817.csv", encoding='utf-8')


def URLDict_to_WordsVector(url_list):
    words_in_page_list = pd.Series(url_list.apply(Get_TitleArticle))
    words_vector_list = pd.DataFrame()
    for i in words_in_page_list:
        words_vector = Keitaiso_Kaiseki(i)
        words_vector_list = pd.concat([words_vector_list, words_vector], axis=1)

    return words_vector_list


def Get_TitleArticle(url):
    '''
    記事のURLを入力すると，その記事のタイトルと記事本文が出力される関数
    :argument url
    :return: Title, Article
    '''
    ssl._create_default_https_context = ssl._create_unverified_context
    try:
        html = urlreq.urlopen(url).read()

        soup = BeautifulSoup(html, 'html.parser')
        # title_part = soup.find_all("h1", {"class": "article_header_title"})
        article_part = soup.find_all("div", {"class": "article gtm-click"})

        # title = title_part[0].get_text()
        article = article_part[0].get_text()

    except:
        article = str(None)

    time.sleep(1)

    words_in_page = article

    return words_in_page


def Keitaiso_Kaiseki(script):
    '''
    出力各記事のデータを形態素解析する．
    その上で名詞のみを取り出し単語別にその回数を数えたものを
    :param script: 
    :return: 
    '''

    m = MeCab.Tagger()
    script = m.parse(script)

    script_list = [word.split('\t') for word in script.split('\n')]
    del script_list[-1]
    del script_list[-1]

    script_df = pd.DataFrame(script_list, columns=['word', 'word_class'])

    script_df['word_class'] = script_df['word_class'].str.split(',')
    script_df['word_class'] = script_df['word_class'].apply(lambda x: x[0])

    script_df_noun = script_df[script_df['word_class'] == '名詞']
    words_vector = script_df_noun.groupby('word').count().sort_values('word_class', ascending=False)

    return words_vector


def main():
    """ 
    Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    """
    Get_Url_List()
    url_dict = pd.read_csv('Gunosy_urllist_0817.csv', header=0, index_col=0)

    for i in url_dict.columns:
        url_list = url_dict[i].dropna()
        words_vector_list = URLDict_to_WordsVector(url_list)
        words_vector_list = words_vector_list.fillna(0)
        code = "words_vector_list.to_csv('words_vector_" + str(i) + ".csv')"
        exec(code)

if __name__ == '__main__':
    main()
