# レシピ管理システム

[Django](https://github.com/django/django) 1.10 を利用したレシピ管理システムです。

## 前提
以下がインストールされていること。

- python3.6
- pip
- nodejs

## セットアップ

1. `pip install django`, `pip install rest_framework`を実行し、ローカルに`django`をインストールします。
2. ルートディレクトリで`npm install`を実行します。
3. 同じくルートディレクトリで`./manage.py runserver`を実行することで、開発サーバを立ち上げられます。

## 注意事項

### タスクランナー

`gulp watch`（または`npm run dev`）を実行すると、SCSS,Vue.jsの変更を監視して`public`ディレクトリに変換後のCSS,JSを出力します。

### ログ出力

環境変数`LOG_DIR`に出力予定です（現在はコンソールのみ）。

### DB接続

MySQLにて`recipe`スキーマを利用します。  
ユーザ・パスワードはアプリケーションが認識可能な環境変数に以下キーで設定してください。  
※Apache・FastCGIなどを利用する場合、そちらに設定すれば取得可能です。

- RECIPE_DB_USER
- RECIPE_DB_PASSWORD

その他環境変数に必要なものがいくつかありますので、`settings.py`を確認してください。