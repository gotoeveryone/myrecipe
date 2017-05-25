""" ログイン用のAPI認証バックエンド """
import requests
from django.conf import settings
from django.http import HttpRequest
from recipe.core.models import MyUser

class WebResourceBackend(object):
    """
    WebリソースAPIを利用した認証クラス
    """

    def authenticate(self, request: HttpRequest, account=None, password=None):
        """
        認証処理
        @param account
        @param password
        """
        # 認証リクエスト
        auth_response = requests.post(settings.API_URL + 'auth/login',\
            {'account': account, 'password': password})

        # 認証エラーの場合
        if auth_response.status_code != 200:
            return None

        # 取得したアクセストークンからユーザ情報を取得
        json = auth_response.json()
        token = json['access_token']

        user_response = requests.get(settings.API_URL + 'users',\
            params={'access_token': token})

        # 取得エラーの場合
        if user_response.status_code != 200:
            return None

        user = MyUser(token, user_response.json())
        request.session['user'] = user

        return user
