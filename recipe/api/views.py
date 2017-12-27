""" APIのビューセット """
from django.http import HttpRequest
from rest_framework import viewsets
from recipe.core.models import Cuisine, Foodstuff
from .serializer import CuisineSerializer, CuisineListSerializer, FoodstuffListSerializer


class CuisineViewSet(viewsets.ModelViewSet):
    """ メニュー REST API """
    queryset = Cuisine.objects
    serializer_class = CuisineSerializer
    user = None

    def dispatch(self, request: HttpRequest, *args, **kwargs):
        self.user = request.META.get('HTTP_X_USERID')
        return super(CuisineViewSet, self).dispatch(request, *args, **kwargs)

    def list(self, request: HttpRequest, *args, **kwargs):
        self.serializer_class = CuisineListSerializer
        return viewsets.ModelViewSet.list(self, request, *args, **kwargs)

    def create(self, request: HttpRequest, *args, **kwargs):
        # 登録ユーザの追加
        request.data['created_by'] = self.user
        request.data['modified_by'] = self.user
        return super(CuisineViewSet, self).create(request, *args, **kwargs)

    def update(self, request: HttpRequest, *args, **kwargs):
        # 更新ユーザの追加
        request.data['modified_by'] = self.user
        return super(CuisineViewSet, self).update(request, *args, **kwargs)

    def get_queryset(self):
        queryset = self.queryset

        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__contains=name)

        classification = self.request.query_params.get('classification')
        if classification:
            queryset = queryset.filter(classification=classification)

        kcal = self.request.query_params.get('kcal')
        if kcal:
            queryset = queryset.filter(ingestion_kcal__lte=kcal)

        return queryset


class FoodstuffViewSet(viewsets.ModelViewSet):
    """ 食材 REST API """
    queryset = Foodstuff.objects.distinct().order_by('name').values('name')
    serializer_class = FoodstuffListSerializer
