# レシピ管理システム #

[Django](https://github.com/django/django) 1.x を利用したレシピ管理システムです。

## 前提
以下がインストールされていること。

- python3.x
- pip
- nodejs

## セットアップ

1. `.env.example`をもとに、`.env`ファイルを生成します。
2. ルートディレクトリで`npm install`を実行します。
3. 以下コマンドを実行して、必要なライブラリを取得します。

```
$ pip install -r setup/requirements.txt
```

## 実行

1. 以下コマンドを実行してください。

```
$ # フロントコード
$ npm run dev
$ # サーバ側
$ ./manage.py runserver
```

### サーバ側でDockerを利用する場合

```
$ cd setup && docker-compose build && docker-compose up
```

### gunicornやwsgiなどで動作させる場合

以下コマンドを実行し、静的ファイルを`static`ディレクトリにまとめます。

```
$ ./manage.py collectstatic
```

## 注意事項

### タスクランナー

`npm run dev`を実行すると、SCSS,TypeScriptの変更を監視して`public`ディレクトリに変換後のCSS,JSを出力します。

### ログ出力

環境変数`LOG_DIR`の下に`recipe.log`というファイル名で出力します。

### DB接続

初期では`MySQL`を利用しますが、必要に応じて変更してください。

その他環境変数については、`settings.py`を確認のうえ、必要に応じて`.env`に環境変数を定義してください。
