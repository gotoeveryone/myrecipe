"""
レシピ関係のアクションマッピング
"""
import logging
from django.shortcuts import render
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
    response = requests.post('https://' + request.get_host() + '/web-resource/users/login',\
        {'account': request.POST['loginid'], 'password': request.POST['password']}, verify=False)

    if response.status_code != 200:
        return render(request, 'error.dhtml', {
            'err': response
        })

    json = response.json()
    request.session['access_token'] = json['access_token']

    # ユーザ情報
    user = requests.get('https://' + request.get_host() + '/web-resource/users/detail',\
        params={'access_token': request.session['access_token']}, verify=False)
    user_info = user.json()
    request.session['user'] = user_info

    logging.info('ユーザ【%s】がログインしました。', user_info['userName'])

    return render(request, 'menu.dhtml', {
        'title': 'メニュー',
        'username': user_info['userName']
    })

def menu(request: HttpRequest):
    """
    メニュー
    @param request
    @return: django template
    """
    return render(request, 'menu.dhtml', {
        'title': 'メニュー'
    })
