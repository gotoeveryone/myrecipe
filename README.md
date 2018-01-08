# MyRecipe

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://github.com/gotoeveryone/myrecipe/blob/master/LICENSE)
[![Dependency Status](https://beta.gemnasium.com/badges/github.com/gotoeveryone/myrecipe.svg)](https://beta.gemnasium.com/projects/github.com/gotoeveryone/myrecipe)
[![GitHub version](https://badge.fury.io/gh/gotoeveryone%2Fmyrecipe.svg)](https://badge.fury.io/gh/gotoeveryone%2Fmyrecipe)

[Django](https://github.com/django/django) 2.x を利用したレシピ管理ツールです。

## 前提
以下がインストールされていること。

- python3.x
- pipenv
- nodejs

## セットアップ

1. `.env.example`をもとに、`.env`ファイルを生成します。
2. ルートディレクトリで`npm install`を実行します。
3. 以下コマンドを実行して、Djangoの実行環境を準備します。

```
$ cd <project_root>
$ pipenv install -d
$
$ # プロジェクト内部に作成する場合は以下を設定
$ PIPENV_VENV_IN_PROJECT=1 pipenv install -d
```

## 実行

1. 以下コマンドを実行してください。

```
$ # フロントコード
$ npm run dev
$ # サーバ側
$ cd <project_root>
$ pipenv run manage.py runserver
```

### サーバ側でDockerを利用する場合

```
$ docker-compose build && docker-compose up
```

### gunicornやwsgiなどで動作させる場合

以下コマンドを実行し、静的ファイルを`static`ディレクトリにまとめます。

```
$ cd <project_root>
$ pipenv run manage.py collectstatic
```

## 注意事項

### タスクランナー

`npm run dev`を実行すると、SCSS,TypeScriptの変更を監視して`public`ディレクトリに変換後のCSS,JSを出力します。

### ログ出力

環境変数`LOG_DIR`の下に`recipe.log`というファイル名で出力します。

### DB接続

初期では`MySQL`を利用しますが、必要に応じて変更してください。

その他環境変数については、`settings.py`を確認のうえ、必要に応じて`.env`に環境変数を定義してください。
