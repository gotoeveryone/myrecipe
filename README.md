# MyRecipe

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://github.com/gotoeveryone/myrecipe/blob/master/LICENSE)
[![GitHub version](https://badge.fury.io/gh/gotoeveryone%2Fmyrecipe.svg)](https://badge.fury.io/gh/gotoeveryone%2Fmyrecipe)

[Django](https://github.com/django/django) 2.x を利用したレシピ管理ツールです。

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
$ # プロジェクト内部に作成する場合は以下を設定
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

```
$ docker-compose build && docker-compose up
```

### gunicorn や wsgi などで動作させる場合

以下コマンドを実行し、静的ファイルを`static`ディレクトリにまとめます。

```
$ cd <project_root>
$ pipenv run cs
```

## Test

```
$ pipenv run t
```

## Notes

### タスクランナー

`yarn run dev`を実行すると、SCSS,TypeScript の変更を監視して`public`ディレクトリに変換後の CSS,JS を出力します。

### ログ出力

環境変数`LOG_DIR`（未定義もしくは空値の場合は`logs`ディレクトリ）に`recipe.log`というファイル名で出力します。

### DB 接続

初期では`MySQL`を利用しますが、必要に応じて変更してください。

その他環境変数については、`settings.py`を確認のうえ、必要に応じて`.env`に環境変数を定義してください。
