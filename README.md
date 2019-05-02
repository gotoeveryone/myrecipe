# MyRecipe

[![Build Status](https://travis-ci.org/gotoeveryone/myrecipe.svg?branch=master)](https://travis-ci.org/cicatrice/travis-test)
[![Heroku](http://heroku-badge.herokuapp.com/?app=myrecipe-k2ss&svg=1)](https://myrecipe-k2ss.herokuapp.com/)
[![Known Vulnerabilities](https://snyk.io/test/github/gotoeveryone/myrecipe/badge.svg)](https://snyk.io/test/github/gotoeveryone/myrecipe)
[![Python Version](https://img.shields.io/badge/python-3.5%20|%203.6%20|%203.7-0366d6.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-2.0-0366d6.svg)](https://docs.djangoproject.com/ja/2.0/)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://github.com/gotoeveryone/myrecipe/blob/master/LICENSE)
[![GitHub version](https://badge.fury.io/gh/gotoeveryone%2Fmyrecipe.svg)](https://badge.fury.io/gh/gotoeveryone%2Fmyrecipe)

[Django](https://github.com/django/django) 2.0 を利用したレシピ管理ツールです。

## Requirements

*   python3.5+
*   pipenv
*   nodejs
*   yarn

## Setup

```console
$ cd <project_root>
$ cp .env.example .env
$ yarn
$ pipenv install -d
$
$ # プロジェクト内部に仮想環境を作成する場合は以下を設定
$ PIPENV_VENV_IN_PROJECT=1 pipenv install -d
```

## Run

```
$ # フロントエンド
$ cd <project_root>
$ yarn run dev
$
$ # バックエンド
$ cd <project_root>
$ pipenv run s
```

### Docker を利用する場合

Python（Django）は`pipenv`を利用するため、データベースのみDockerイメージを用意しています。

```
$ cd <project_root>/docker
$ docker-compose up -d
```

### gunicorn や wsgi などで動作させる場合

以下コマンドを実行し、静的ファイルを`static`ディレクトリにまとめます。

```
$ cd <project_root>
$ pipenv run cs
```

## Test

```
$ cd <project_root>
$ pipenv run test
```

## Notes

### タスクランナー

`yarn run dev`を実行すると、SCSS,TypeScript の変更を監視して`static`ディレクトリに変換後の CSS,JS を出力します。

### ログ出力

環境変数`LOG_DIR`（未定義もしくは空値の場合は`logs`ディレクトリ）に`recipe.log`というファイル名で出力します。

### DB 接続

初期では`PostgreSQL`を利用します。

その他環境変数については、`settings.py`を確認のうえ、必要に応じて`.env`に環境変数を定義してください。
