"""
カスタムミドルウェア
"""
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject

def get_user(request):
    """
    ユーザ取得処理
    セッションからユーザオブジェクトを取得し返却
    セッションに存在しない場合はauthモジュールに処理を委譲する
    """
    from django.contrib import auth

    user = request.session.get('user')
    if user is not None:
        return user

    return auth.get_user(request)

class AuthenticationMiddleware(MiddlewareMixin):
    """
    独自の認証ミドルウェア
    """
    def process_request(self, request):
        """
        リクエスト時の処理
        """
        assert hasattr(request, 'session'), (
            "The Django authentication middleware requires session middleware "
            "to be installed. Edit your MIDDLEWARE%s setting to insert "
            "'django.contrib.sessions.middleware.SessionMiddleware' before "
            "'django.contrib.auth.middleware.AuthenticationMiddleware'."
        ) % ("_CLASSES" if settings.MIDDLEWARE is None else "")
        request.user = SimpleLazyObject(lambda: get_user(request))
