from logging import getLogger
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import exception_handler


def response401():
    """ 認証エラーレスポンスを返却 """
    return JsonResponse({
        'code': status.HTTP_401_UNAUTHORIZED,
        'message': '認証エラーです。',
    }, status=status.HTTP_401_UNAUTHORIZED)


def custom_exception_handler(exc, context):
    """ 例外ハンドラ """
    response = exception_handler(exc, context)

    if response:
        if response.status_code in [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN]:
            return response401()

        if response.status_code == status.HTTP_404_NOT_FOUND:
            return JsonResponse({
                'code': status.HTTP_404_NOT_FOUND,
                'message': 'ページが見つかりません。',
            }, status=status.HTTP_404_NOT_FOUND)

        if response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED:
            return JsonResponse({
                'code': status.HTTP_405_METHOD_NOT_ALLOWED,
                'message': '許可されていないリクエストです。',
            }, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    logger = getLogger(__name__)
    logger.error(exc)
    return JsonResponse({
        'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
        'message': '内部サーバーエラーです。管理者にご確認ください。',
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
