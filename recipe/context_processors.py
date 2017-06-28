"""
環境変数をテンプレートで利用するためのプロセッサ
"""
from django.conf import settings

def site_common(request):
    """ サイト共通 """
    return {'ASSETS_URL': settings.ASSETS_URL}
