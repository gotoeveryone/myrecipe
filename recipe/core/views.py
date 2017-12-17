"""
レシピ関係のアクションマッピング
"""
from logging import getLogger
from django.conf import settings
from django.contrib import auth, messages
from django.contrib.messages import get_messages
from django.shortcuts import render, redirect
from django.http import HttpRequest
from recipe.core.forms import LoginForm


def index(request: HttpRequest, form=None):
    """
    初期表示
    @param request
    @param form
    @return: django template
    """
    if request.session.get('user'):
        return redirect('recipe_cuisine:index')

    return render(request, 'index.dhtml', {
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

    user = auth.authenticate(request,
                        username=form.cleaned_data['account'],
                        password=form.cleaned_data['password'])

    if user is None:
        messages.add_message(request, messages.ERROR, 'ログインに失敗しました。')
        return index(request, form)

    auth.login(request, user, backend=user.backend)

    logger = getLogger(__name__)
    logger.info('ユーザ【%s】がログインしました。', user.get_username())

    next_url = request.POST.get('next', '')
    if next_url == "":
        next_url = 'recipe_cuisine:index'

    # Cookieにログインユーザを設定してリダイレクト
    response = redirect(next_url)
    logger.info(user.get_username())
    response.set_cookie(
        'account', value=user.get_username(), max_age=settings.SESSION_COOKIE_AGE)
    return response


def logout(request: HttpRequest):
    """
    ログアウト
    @param request
    @return: django template
    """
    auth.logout(request)

    response = redirect('recipe:index')
    response.delete_cookie('account')
    return response
