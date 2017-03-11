"""
レシピ関係のアクションマッピング
"""
from django.shortcuts import render, Http404
from django.http import HttpRequest
import requests
from .models import Cuisine, Instruction, Quantity
from .forms import CuisineForm

def index(request: HttpRequest):
    """
    初期表示
    @param request
    @return: django template
    """
    return render(request, 'index.html', {'title': 'ログイン'})

def login(request: HttpRequest):
    """
    ログイン
    @param request
    @return: django template
    """
    response = requests.post('https://' + request.get_host() + '/web-resource/users/login',\
        {'account': request.POST['loginid'], 'password': request.POST['password']}, verify=False)

    if response.status_code != 200:
        return render(request, 'error.html', {
            'err': response
        })

    json = response.json()
    request.session['access_token'] = json['access_token']

    # ユーザ情報
    user = requests.get('https://' + request.get_host() + '/web-resource/users/detail',\
        params={'access_token': request.session['access_token']}, verify=False)

    request.session['user'] = user.json()

    return render(request, 'menu.html', {
        'title': 'メニュー',
        'username': request.session['user']['userName']
    })

def menu(request: HttpRequest):
    """
    メニュー
    @param request
    @return: django template
    """
    return render(request, 'menu.html', {
        'title': 'メニュー'
    })

def cuisine(request: HttpRequest):
    """
    料理一覧初期表示
    @param request
    @return: django template
    """
    return render(request, 'cuisine/index.html', {
        'title': 'レシピ一覧',
        'form': CuisineForm(),
        'classifications': ['主菜', '副菜', '主食', 'デザート', 'その他'],
    })

def cuisine_search(request: HttpRequest):
    """
    料理検索
    @param request
    @return: django template
    """
    if request.method != 'POST':
        return cuisine(request)

    form = CuisineForm(request.POST)
    obj = Cuisine.objects

    if form.is_valid():

        # 値を取得
        name = form.cleaned_data['name']
        classification = form.cleaned_data['classification']
        ingestion_kcal = form.cleaned_data['ingestion_kcal']

        # フィルタ
        obj = obj.filter(name__contains=name) if name else obj
        obj = obj.filter(classification__exact=classification) if classification else obj
        obj = obj.filter(ingestion_kcal__exact=ingestion_kcal) if ingestion_kcal else obj

    print(obj.all().query)

    return render(request, 'cuisine/index.html', {
        'title': 'レシピ一覧',
        'form': form,
        'cuisines': obj.all()
    })

def cuisine_edit(request: HttpRequest, primary_key: int):
    """
    料理編集
    @param request
    @param int
    @return: django template
    """
    try:
        model = Cuisine.objects.get(pk=primary_key)

        # 手順
        instructions = Instruction.objects.filter(cuisine=model).order_by('sort_order')
        model.instructions_set = instructions

        # 数量・食材
        quantities = Quantity.objects.filter(cuisine=model).prefetch_related('foodstuff')
        model.quantities_set = quantities

        print(quantities.query)
    except Cuisine.DoesNotExist:
        raise Http404

    return render(request, 'cuisine/edit.html', {
        'title': 'レシピ編集',
        'cuisine': model,
    })
