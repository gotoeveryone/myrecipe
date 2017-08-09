""" ログイン用のAPI認証バックエンド """
import requests
from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.http import HttpRequest
from recipe.core.models import MyUser


class WebResourceBackend(ModelBackend):
    """
    WebリソースAPIを利用した認証クラス
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        認証処理
        @param request
        @param username
        @param password
        @param kwargs
        """
        # 認証リクエスト
        url = '%sauth/login' % settings.API_URL
        auth_response = requests.post(
            url, {'account': username, 'password': password})

        # 認証エラーの場合
        if auth_response.status_code != 200:
            return None

        # 取得したアクセストークンからユーザ情報を取得
        json = auth_response.json()
        token = json['access_token']

        user_url = '%susers' % settings.API_URL
        user_response = requests.get(
            user_url, headers={'Authorization': 'Bearer %s' % token})

        # 取得エラーの場合
        if user_response.status_code != 200:
            return None

        user = MyUser(token, user_response.json())
        request.session['user'] = user

        return user

    def has_module_perms(self, user_obj, app_label):
        """
        管理画面へのアクセス許可
        @param user_obj
        @param app_label
        """
        if not user_obj.is_active or not user_obj.is_superuser:
            return False
        return True
