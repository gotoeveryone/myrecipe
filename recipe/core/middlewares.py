"""
スレッドローカルなオブジェクトを持ちまわすためのミドルウェアクラス
"""
from django.utils.deprecation import MiddlewareMixin

try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local

_thread_locals = local()

def get_current_request():
    """ returns the request object for this thread """
    return getattr(_thread_locals, "request", None)

def get_current_user():
    """ returns the current user, if exist, otherwise returns None """
    request = get_current_request()
    if request:
        return getattr(request, "user", None)

class ThreadLocalMiddleware(MiddlewareMixin):
    """ Simple middleware that adds the request object in thread local storage."""
    def process_request(self, request):
        """
        リクエストを保持します。
        @param request
        """
        _thread_locals.request = request

    def process_response(self, request, response):
        """
        保持しているリクエストを削除し、レスポンスを返却します。
        @param request
        @param response
        """
        self.delete_request()
        return response

    def process_exception(self, request, exception):
        """
        保持しているリクエストを削除し、レスポンスを返却します。
        @param request
        @param exception
        """
        self.delete_request()

    def delete_request(self):
        """
        保持しているリクエストを削除します。
        """
        if hasattr(_thread_locals, 'request'):
            del _thread_locals.request
