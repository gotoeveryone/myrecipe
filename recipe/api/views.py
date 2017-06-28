""" APIのビューセット """
from rest_framework import viewsets
from recipe.core.models import Cuisine, Instruction, Quantity, Foodstuff
from .serializer import CuisineSerializer, CuisineListSerializer,\
    InstructionSerializer, QuantitySerializer, FoodstuffSerializer

class CuisineViewSet(viewsets.ModelViewSet):
    """ メニュー REST API """
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = CuisineListSerializer
        return viewsets.ModelViewSet.list(self, request, *args, **kwargs)

    def get_queryset(self):
        queryset = self.queryset

        name = self.request.query_params.get('name')
        if name:
            queryset = self.queryset.filter(name=name)

        classification = self.request.query_params.get('classification')
        if classification:
            queryset = self.queryset.filter(classification=classification)

        kcal = self.request.query_params.get('kcal')
        if kcal:
            queryset = self.queryset.filter(ingestion_kcal=kcal)

        return queryset

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

class FoodstuffViewSet(viewsets.ModelViewSet):
    """ 食材 REST API """
    queryset = Foodstuff.objects.all()
    serializer_class = FoodstuffSerializer
    filter_fields = ('id')
