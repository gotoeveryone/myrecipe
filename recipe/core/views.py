"""
レシピ関係のアクションマッピング
"""
import logging
from django.conf import settings
from django.contrib.auth import authenticate, login as logged, logout as logged_out
from django.contrib import messages
from django.contrib.messages import get_messages
from django.shortcuts import render, redirect
from django.http import HttpRequest
import requests
from recipe.core.forms import LoginForm

def index(request: HttpRequest, form=None):
    """
    初期表示
    @param request
    @param form
    @return: django template
    """
    return render(request, 'index.dhtml', {
        'title': 'ログイン',
        'form': LoginForm() if form is None else form,
        'messages': get_messages(request),
    })

def login(request: HttpRequest):
    """
    ログイン
    @param request
    @return: django template
    """
    form = LoginForm(request.POST)
    if not form.is_valid():
        messages.add_message(request, messages.ERROR, 'ログインに失敗しました。')
        return index(request, form)

    user = authenticate(request,\
        account=form.cleaned_data['account'],\
        password=form.cleaned_data['password'])

    if user is None:
        messages.add_message(request, messages.ERROR, 'ログインに失敗しました。')
        return index(request, form)

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
    # トークンを保持していれば削除リクエストを投げる
    user = request.session.get('user')
    if user is not None:
        url = '%sauth/logout' % settings.API_URL
        requests.delete(url, headers={'Authorization': 'Bearer %s' % user.token})

    logged_out(request)

    return redirect('recipe:index')

def menu(request: HttpRequest):
    """
    メニュー
    @param request
    @return: django template
    """
    return render(request, 'menu.dhtml', {
        'title': 'メニュー'
    })
