"""
カスタムミドルウェア
"""
import json
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject
from recipe.core.models import ApiUser


class WebApiAuthenticationMiddleware(MiddlewareMixin):
    """
    API認証ミドルウェア
    """

    def process_request(self, request):
        """
        リクエスト時の処理
        @param request
        """
        assert hasattr(request, 'session'), (
            "The Django authentication middleware requires session middleware "
            "to be installed. Edit your MIDDLEWARE%s setting to insert "
            "'django.contrib.sessions.middleware.SessionMiddleware' before "
            "'recipe.middlewares.WebApiAuthenticationMiddleware'."
        ) % ("_CLASSES" if settings.MIDDLEWARE is None else "")
        request.user = SimpleLazyObject(lambda: self.get_user(request))

    def get_user(self, request):
        """
        セッションからログインユーザを取得する
        @param request
        """
        from django.contrib.auth.models import AnonymousUser
        user_data = request.session.get('user')
        if not user_data:
            return AnonymousUser()

        return ApiUser().from_json(json.loads(user_data))
