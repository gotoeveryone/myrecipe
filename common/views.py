"""
レシピ関係のアクションマッピング
"""
import logging
from django.contrib.auth import authenticate, login as logged, logout as logged_out
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpRequest
import requests

def index(request: HttpRequest):
    """
    初期表示
    @param request
    @return: django template
    """
    return render(request, 'index.dhtml', {'title': 'ログイン'})

def login(request: HttpRequest):
    """
    ログイン
    @param request
    @return: django template
    """
    user = authenticate(request,\
        account=request.POST['loginid'], password=request.POST['password'])

    if user is None:
        return render(request, 'error.dhtml')

    request.session['user'] = user
    logged(request, user, backend=user.backend)

    logger = logging.getLogger('recipe')
    logger.info('ユーザ【%s】がログインしました。', user.user_name)

    next_url = request.POST.get('next', '')
    if next_url != '':
        return redirect(next_url)

    return render(request, 'menu.dhtml', {
        'title': 'メニュー'
    })

def logout(request: HttpRequest):
    """
    ログアウト
    @param request
    @return: django template
    """
    api_url = 'https://' + request.get_host() + '/web-resource/'

    # トークンを保持していれば削除リクエストを投げる
    if request.session.get('access_token') is not None:
        requests.post(api_url + 'users/logout',\
            {'access_token': request.session['access_token']}, verify=False)

    logged_out(request)

    return render(request, 'index.dhtml', {'title': 'ログイン'})

@login_required
def menu(request: HttpRequest):
    """
    メニュー
    @param request
    @return: django template
    """
    return render(request, 'menu.dhtml', {
        'title': 'メニュー'
    })
