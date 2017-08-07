"""
カスタムミドルウェア
"""
from django.contrib import auth
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject
from django.contrib.auth.middleware import RemoteUserMiddleware


class WebResourceMiddleware(MiddlewareMixin):
    """
    独自の認証ミドルウェア
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
            "'recipe.middlewares.WebResourceMiddleware'."
        ) % ("_CLASSES" if settings.MIDDLEWARE is None else "")
        request.user = SimpleLazyObject(lambda: self.get_user(request))

    def get_user(self, request):
        """
        セッションからログインユーザを取得する
        @param request
        """
        from django.contrib.auth.models import AnonymousUser
        return request.session.get('user') or AnonymousUser()
