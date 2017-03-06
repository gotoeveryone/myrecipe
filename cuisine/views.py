"""
レシピ関係のアクションマッピング
"""
from django.shortcuts import render, Http404
from django.http import HttpRequest
from .models import Cuisine, CuisineForm

def index(request: HttpRequest):
    """ 初期表示 """

    return render(request, 'cuisine/index.html', {
        'title': 'レシピ一覧',
        'form': CuisineForm(),
        'cuisines': Cuisine.objects.all(),
        'classifications': ['主菜', '副菜', '主食', 'デザート', 'その他'],
    })

def search(request: HttpRequest):
    """ 検索 """

    if request.method != 'POST':
        index(request)

    form = CuisineForm(request.POST)
    obj = Cuisine.objects

    print(form.fields)

    if form.is_valid():
        print(form.cleaned_data)
        name = form.cleaned_data['name']
        classification = form.cleaned_data['classification']
        ingestion_kcal = form.cleaned_data['ingestion_kcal']

        if name:
            obj = obj.filter(name__contains=name)
        if classification:
            obj = obj.filter(classification__exact=classification)
        if ingestion_kcal:
            obj = obj.filter(ingestion_kcal__exact=ingestion_kcal)

    print(obj.all().query)

    return render(request, 'cuisine/index.html', {
        'title': 'レシピ一覧',
        'form': form,
        'cuisines': obj.all()
    })

def edit(request: HttpRequest, id: int):
    """ 編集 """

    try:
        obj = Cuisine.objects.get(pk=id)
    except Cuisine.DoesNotExist:
        raise Http404

    return render(request, 'cuisine/edit.html', {
        'title': 'レシピ編集',
        'cuisine': obj,
    })
