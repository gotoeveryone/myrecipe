# MyRecipe

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://github.com/gotoeveryone/myrecipe/blob/master/LICENSE)
[![Dependency Status](https://beta.gemnasium.com/badges/github.com/gotoeveryone/myrecipe.svg)](https://beta.gemnasium.com/projects/github.com/gotoeveryone/myrecipe)
[![GitHub version](https://badge.fury.io/gh/gotoeveryone%2Fmyrecipe.svg)](https://badge.fury.io/gh/gotoeveryone%2Fmyrecipe)

[Django](https://github.com/django/django) 2.x を利用したレシピ管理ツールです。

## 前提

以下がインストールされていること。

*   python3.5+
*   pipenv
*   nodejs

## セットアップ

1.  `.env.example`をもとに、`.env`ファイルを生成します。
2.  ルートディレクトリで`npm install`を実行します。
3.  以下コマンドを実行して、Django の実行環境を準備します。

```
$ cd <project_root>
$ pipenv install -d
$
$ # プロジェクト内部に作成する場合は以下を設定
$ PIPENV_VENV_IN_PROJECT=1 pipenv install -d
```

## 実行

```
$ # フロントコード
$ cd <project_root>
$ npm run dev
$ # サーバ側
$ cd <project_root>
$ pipenv run manage.py runserver
```

### Docker を利用する場合

```
$ docker-compose build && docker-compose up
```

### gunicorn や wsgi などで動作させる場合

以下コマンドを実行し、静的ファイルを`static`ディレクトリにまとめます。

```
$ cd <project_root>
$ pipenv run manage.py collectstatic
```

## テスト

```
$ pipenv run manage.py test
```

## 注意事項

### タスクランナー

`npm run dev`を実行すると、SCSS,TypeScript の変更を監視して`public`ディレクトリに変換後の CSS,JS を出力します。

### ログ出力

環境変数`LOG_DIR`（未定義もしくは空値の場合は`logs`ディレクトリ）に`recipe.log`というファイル名で出力します。

### DB 接続

初期では`MySQL`を利用しますが、必要に応じて変更してください。

その他環境変数については、`settings.py`を確認のうえ、必要に応じて`.env`に環境変数を定義してください。
