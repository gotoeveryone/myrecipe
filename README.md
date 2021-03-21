# MyRecipe

![Myrecipe Build](https://github.com/gotoeveryone/myrecipe/workflows/Myrecipe%20Build/badge.svg)
[![Known Vulnerabilities](https://snyk.io/test/github/gotoeveryone/myrecipe/badge.svg)](https://snyk.io/test/github/gotoeveryone/myrecipe)
[![Python Version](https://img.shields.io/badge/python-3.5%20|%203.6%20|%203.7-0366d6.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-2.0-0366d6.svg)](https://docs.djangoproject.com/ja/2.0/)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://github.com/gotoeveryone/myrecipe/blob/master/LICENSE)
[![GitHub version](https://badge.fury.io/gh/gotoeveryone%2Fmyrecipe.svg)](https://badge.fury.io/gh/gotoeveryone%2Fmyrecipe)

[Django](https://github.com/django/django) 2.0 を利用したレシピ管理ツールです。

## Requirements

- Docker

## Setup

```console
$ cp .env.example .env
```

## Run

```
$ docker-compose up
```

- ホストから接続するためのポートは以下
  - ブラウザ: 8000
  - データベース: 15432

## Migration

```console
$ docker-compose exec backend pipenv run pm migrate
```

## Create administrator

```
$ docker-compose exec backend pipenv run pm createsuperuser
```

## Test

```
$ docker-compose exec backend pipenv run pm test
```

## Collect static files

以下コマンドを実行し、静的ファイルを`static`ディレクトリにまとめます。

```
$ docker-compose exec backend pipenv run pm collectstatic
```

## Notes

### DB 接続

初期では`PostgreSQL`を利用します。

その他環境変数については、`settings.py`を確認のうえ、必要に応じて`.env`に環境変数を定義してください。
