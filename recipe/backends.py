""" ログイン用のAPI認証バックエンド """
import json
from logging import getLogger
import requests
from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from recipe.core.models import User


@receiver(user_logged_out)
def deauthenticate(request, **kwargs):
    """
    認証解除処理
    :param request
    :param kwargs
    """
    user = getattr(request, 'user', None)

    # APIの認証解除
    if isinstance(user, User):
        url = '%sdeauth' % settings.API_URL
        response = requests.delete(
            url, headers={'Authorization': 'Bearer %s' % user.get_access_token()})

        if not response.ok:
            logger = getLogger(__name__)
            logger.error(response.json())


class WebApiBackend(ModelBackend):
    """
    WebAPIを利用した認証クラス
    """
    logger = getLogger(__name__)

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        認証処理
        :param request
        :param username
        :param password
        :param kwargs
        :return MyUser or None
        """
        # 認証リクエスト
        url = '%sauth' % settings.API_URL
        auth_response = requests.post(
            url, json={'account': username, 'password': password})

        # アクセストークン取得エラー
        if not auth_response.ok:
            self.logger.error(auth_response.json())
            return None

        # 取得したアクセストークンからユーザ情報を取得
        token = auth_response.json().get('accessToken')
        user_url = '%susers' % settings.API_URL
        user_response = requests.get(
            user_url, headers={'Authorization': 'Bearer %s' % token})

        # ユーザ情報取得エラー
        if not user_response.ok:
            self.logger.error(user_response.json())
            return None

        user_json = user_response.json()
        user_json['accessToken'] = token

        # DBに保存したIDを取得する（管理画面用）
        db_user, _ = User.objects.get_or_create(**{
            User.USERNAME_FIELD: username
        })
        user_json['id'] = db_user.pk

        # メールアドレスを保存
        user = User().from_json(user_json)
        db_user.email = user.email
        db_user.save()

        request.session['user'] = json.dumps(user.to_json())
        return user
