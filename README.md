naive_bayes_classifier_for_news_articles
==============================
# Naive bayes classifier for categorize news articles
やること：ニュースサイトの記事をカテゴリ分類するための，単純ベイズを用いた分類機を作成する．

### やり方

#### データの取得
今回は，https://gunosy.com/ 上の記事を用いる．
まずは,URLを入れたら記事がデータとして出てくるようにする．

* File Name : URLのhttps://gunosy.com/articles/ 以降 exam>> "<b>Ryw5G</b>"
* File Content :
  - Title   :    
  Xpath:  /html/body/div[7]/div[1]/div[2]/div[2]/h1  
  {\h1 class="article_header_title"}

  - Article :  
  Xpath:  /html/body/div[7]/div[2]/div/div[1]/div[2]
  {\div class="article gtm-click"}

Xpath & lxmlでは，取り出せなかったのでふつーにBeautifulSoupで取り出しました．

#### 単語への分割
    MeCabを使用して


#### 分類機の作成
今回は，ナイーブベイズを使った分類器を作成する

- 2で使用する教師あり文書分類器は、事前に学習しておく必要があります。教師データは、 https://gunosy.com/ の「エンタメ」、「スポーツ」、「おもしろ」、「国内」、「海外」、「コラム」、「IT・科学」、「グルメ」の記事を使用して下さい。
- 教師データの収集、分類器の学習はDjangoのカスタムコマンドとして実行できるようにしてください
- 分類器は何らかの評価指標を用いて、評価をして下さい。



A short description of the project.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- "make data"や"make train"のようなコマンドでMakefileを作成する
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
