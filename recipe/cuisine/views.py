"""
    メニュー関連
"""
from django.shortcuts import render
from django.http import HttpRequest
from django.views import generic
from recipe.core.models import Cuisine

class CuisineListView(generic.ListView):
    """ 料理一覧 """
    model = Cuisine
    template_name = 'cuisine/index.dhtml'

    def __init__(self):
        self.title = '料理一覧'

    def get(self, request: HttpRequest, *args, **kwargs):
        return render(request, self.template_name, {
            'title': self.title,
        })

class CuisineAddView(generic.CreateView):
    """ 料理追加 """
    model = Cuisine
    template_name = 'cuisine/detail.dhtml'
    fields = ['name', 'classification', 'ingestion_kcal', 'create_number_of_times']

    def __init__(self):
        self.title = '料理追加'

class CuisineDetailView(generic.detail.DetailView):
    """ 料理詳細 """
    model = Cuisine
    template_name = 'cuisine/detail.dhtml'

    def __init__(self):
        self.title = '料理詳細'

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.render_view(request, **kwargs)

    def render_view(self, request: HttpRequest, **kwargs):
        """ 描画処理 """
        return render(request, self.template_name, {
            'title': self.title,
            'id': kwargs.get('pk', ''),
        })
