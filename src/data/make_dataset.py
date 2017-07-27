# -*- coding: utf-8 -*-
import os
import click
import logging
import urllib.request as urlreq
from bs4 import BeautifulSoup
import ssl


#@click.command()
#@click.argument('input_filepath', type=click.Path(exists=True))
#@click.argument('output_filepath', type=click.Path())

def get_url():
    ssl._create_default_https_context = ssl._create_unverified_context
    print("カテゴリ分類を行いたい記事のURLを入力してください．")
    url = str("https://" + input())
    html = urlreq.urlopen(url).read()

    soup = BeautifulSoup(html,"lxml")
    title = soup.find_all("h1", {"class": "article_header_title"})
    article = soup.find_all("div", {"class": "article gtm-click"})

    print(title[0].get_text())
    print(article[0].get_text())

    return url

    # https://gunosy.com/articles/Ryw5G
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')


if __name__ == '__main__':
    url = get_url()


    #logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    #load_dotenv(find_dotenv())

    #main()
