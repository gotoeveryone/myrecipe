"""
レシピ関係のアクションマッピング
"""
from django import forms
from django.shortcuts import render, Http404
from django.http import HttpRequest
from django.views import generic
from rest_framework import viewsets
import requests
from .models import Cuisine, Instruction, Quantity, Foodstuff
from .forms import CuisineForm
from .serializer import CuisineSerializer, InstructionSerializer, QuantitySerializer

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

class CuisineListView(generic.ListView):
    """ 料理一覧 """
    model = Cuisine
    form_class = CuisineForm
    template_name = 'cuisine/index.html'

    def __init__(self):
        self.title = 'レシピ一覧'
        self.classifications = ['主菜', '副菜', '主食', 'デザート', 'その他']

    def get(self, request: HttpRequest, *args, **kwargs):
        """ 初期表示 """
        return render(request, self.template_name, {
            'title': self.title,
            'form': self.form_class(),
            'classifications': self.classifications,
        })

    def post(self, request: HttpRequest, *args, **kwargs):
        """ 検索 """
        form = self.form_class(request.POST)
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

        return render(request, self.template_name, {
            'title': self.title,
            'form': form,
            'cuisines': obj.all(),
            'classifications': self.classifications,
        })

def cuisine_add(request: HttpRequest):
    """
    料理追加
    @param request
    @return: django template
    """
    return render(request, 'cuisine/edit.html', {
        'title': 'レシピ追加',
        'cuisine': Cuisine(),
        'classification': (('', ''), ('1', '主菜'), ('2', '主食'), ('3', '副菜'), ('4', 'デザート')),
    })

class CuisineDetailView(generic.edit.UpdateView):
    """ レシピ詳細ビュー """
    model = Cuisine
    template_name = 'cuisine/edit.html'
    success_url = 'cuisine/edit.html'
    # fields = ['name', 'classification', 'ingestion_kcal', 'create_number_of_times']

    def __init__(self):
        self.title = 'レシピ詳細'
        self.classifications = ['主菜', '副菜', '主食', 'デザート', 'その他']

    def post(self, request: HttpRequest, *args, **kwargs):

        # 料理
        cuisine = Cuisine.objects.get(pk=kwargs['pk'])
        cuisine.name = request.POST.get('name')
        cuisine.classification = request.POST.get('classification')
        cuisine.ingestion_kcal = request.POST.get('ingestion_kcal')
        cuisine.create_number_of_times = request.POST.get('create_number_of_times')
        cuisine.save()

        # 調理手順
        instructions = Instruction.objects.filter(cuisine=cuisine).order_by('sort_order')
        input_description = request.POST.getlist('instructions.description')
        for idx, obj in enumerate(input_description):
            print(idx, obj)
            if len(instructions) < idx + 1:
                item = Instruction()
                item.cuisine = cuisine
            else:
                item = instructions[idx]

            item.sort_order = idx + 1
            item.description = obj
            item.save()

        # 食材・分量
        quantities = Quantity.objects.filter(cuisine=cuisine)
        input_detail = request.POST.getlist('quantities.detail')
        input_foodstuff = request.POST.getlist('quantities.foodstuff.name')
        input_classification = request.POST.getlist('quantities.foodstuff.classification')
        for idx, obj in enumerate(input_detail):
            if len(quantities) < idx + 1:
                item = Quantity()
                item.cuisine = cuisine
            else:
                item = quantities[idx]

            # 食材
            foodstuff = Foodstuff.objects.get(quantity=item)
            if foodstuff is None:
                foodstuff = Foodstuff()

            foodstuff.name = input_foodstuff[idx]
            foodstuff.classification = input_classification[idx]
            foodstuff.save()

            item.detail = obj
            item.save()

        return render(request, self.template_name, {
            'title': self.title,
            'cuisine': self.get_object(),
            'classification': self.classifications,
        })

    def get(self, request: HttpRequest, *args, **kwargs):
        return render(request, self.template_name, {
            'title': self.title,
            'cuisine': self.get_object(),
            'classification': self.classifications,
        })

    def get_object(self, queryset=None):
        target = super(CuisineDetailView, self).get_object(queryset)

        # 手順
        instructions = Instruction.objects.filter(cuisine=target).order_by('sort_order')
        target.instructions_set = instructions

        # 数量・食材
        quantities = Quantity.objects.filter(cuisine=target).prefetch_related('foodstuff')
        target.quantities_set = quantities

        return target

def cuisine_save(request: HttpRequest):
    """
    料理一覧初期表示
    @param request
    @return: django template
    """
    cuisine = Cuisine(request.POST)
    print(cuisine)
    return render(request, 'cuisine/edit.html', {
        'title': 'レシピ一覧',
        'form': CuisineForm(),
        'classifications': ['主菜', '副菜', '主食', 'デザート', 'その他'],
    })

class CuisineViewSet(viewsets.ModelViewSet):
    """ メニュー REST API """
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer
    filter_fields = ('cuisine_id')

class InstructionViewSet(viewsets.ModelViewSet):
    """ 調理手順 REST API """
    queryset = Instruction.objects.all()
    serializer_class = InstructionSerializer
    filter_fields = ('cuisine_id')

class QuantityViewSet(viewsets.ModelViewSet):
    """ 調理手順 REST API """
    queryset = Quantity.objects.all()
    serializer_class = QuantitySerializer
    filter_fields = ('id')
