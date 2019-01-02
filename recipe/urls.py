"""recipe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.conf.urls import handler500
from django.contrib import admin
from recipe import settings

urlpatterns = [
    path('', include('recipe.core.urls')),
    path('api/', include('recipe.api.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


def error(request):
    """ 500エラー時は詳細なエラーをログ出力する """
    from logging import getLogger
    import traceback
    from django.shortcuts import render_to_response

    logger = getLogger(__name__)
    logger.error(traceback.format_exc())

    return render_to_response('error.dhtml')


handler500 = 'recipe.urls.error'
