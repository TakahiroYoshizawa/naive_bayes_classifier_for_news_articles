naive_bayes_clf_for_news_articles
==============================
# 課題
- Step1: 記事URLを入れると記事カテゴリを返す、ナイーブベイズを使った教師あり文書分類器ウェブアプリの実装
- Step2: 文書分類性能の改善

# 具体的な要件
## 環境
- Python 3.6
- Django 1.11
- その他ライブラリは自由に使用可能
- ナイーブベイズを使った教師あり文書分類器は、scikit-learnやgensimなどの機械学習ライブラリを使用せず、独自実装してください。
- NumpyやScipy、TensorFlowなどの数値計算ライブラリの使用は可能です。
- 分類性能を改善する際には、機械学習ライブラリを使用しても構いません。

## Step1: ウェブアプリの具体的な処理について
### ウェブアプリの機能
1. フォームから記事URLを入力する。
2. 1で入力された記事URLのHTMLを取得し、それを元に、記事カテゴリを判定する。
3. 2で判定したカテゴリを画面に出力する。

### ナイーブベイズを使った分類器の作成
- 2で使用する教師あり文書分類器は、事前に学習しておく必要があります。教師データは、 https://gunosy.com/ の「エンタメ」、「スポーツ」、「おもしろ」、「国内」、「海外」、「コラム」、「IT・科学」、「グルメ」の記事を使用して下さい。
- 教師データの収集、分類器の学習はDjangoのカスタムコマンドとして実行できるようにしてください
- 分類器は何らかの評価指標を用いて、評価をして下さい。

## Step2: 分類器の精度向上
- どんな方法でもいいので、なんらかの工夫をして精度を向上させる
- ナイーブベイズでなくて、異なる手法を用いても良い。
- その際に機械学習ライブラリを用いてもよい
- Step1で作成した分類器と精度の比較ができるようにしておく

## コード規約
- PEP8に従っていること
- travis-ciなどを用いて自動でPEP8のチェックを行えるようにしてください
- docstringが書かれていること
- 変数名、関数名が明確であること
- マジックナンバーが使われていないこと
- 定数はenumを使って分離することを推奨します
- 使ったライブラリはrequirements.txtとして記載してください
- setup.pyでも可
- 不要なファイルは.gitignoreにかかれており、コミットされていない
- READMEが書かれている
- 環境構築の方法
- 動作させるための方法
- 作った分類器の精度

# 成果物
- ソースコード（GitHubに上げる）
- GitHubはプライベートレポジトリで作成する
- 精度向上のために、行った工夫と実際の精度についてREADMEに記載してください

# 期間
★★8月18日(金)★★

# 評価基準
- Git、Githubの基本的な使い方を理解している。
- Pythonの基本的な実装ができる。
- Webアプリケーションフレームワークの仕組みを理解している。
- 教師あり文書分類器の仕組みを理解している。
- 教師データとテストデータを分離して、精度を検証しなければならないことを理解している。
- 精度向上のために、試行錯誤ができている





A short description of the project.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
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
