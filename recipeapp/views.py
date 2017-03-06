from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    """Index

    :param request
    :return: django template
    """
    return render(request, 'recipe/index.html', {'title': 'ログイン'})

def login(request):
    """Login

    :param request
    :return: django template
    """

    response = requests.post("https://local.kazukisv.com/web-resource/users/login", \
        {'account': 'k-amago', 'password': 'kazuki11'}, verify=False)

    if response.status_code != 200:
        return render(request, 'recipe/error.html', {
            'err': response
        })

    json = response.json()
    request.session['access_token'] = json['access_token']

    # ユーザ情報
    user = requests.get("https://local.kazukisv.com/web-resource/users/detail", \
        params={'access_token': request.session['access_token']}, verify=False)

    request.session['user'] = user.json()

    return render(request, 'recipe/menu.html', {
        'title': 'メニュー',
        'username': request.session['user']['userName']
    })

def search_cuisine(request):
    return render(request, 'recipe/cuisine/search.html', {
        'title': 'レシピ一覧',
        'username': request.session['user']['userName']
    })
