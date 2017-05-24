""" APIのビューセット """
from rest_framework import viewsets
from recipe.core.models import Cuisine, Instruction, Quantity, Foodstuff
from .serializer import CuisineSerializer, InstructionSerializer,\
    QuantitySerializer, FoodstuffSerializer

class CuisineViewSet(viewsets.ModelViewSet):
    """ メニュー REST API """
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer
    filter_fields = ('cuisine_id')

    def get_serializer_context(self):
        print(self.request.user)
        return super(CuisineViewSet, self).get_serializer_context()

    def dispatch(self, *args, **kwargs):
        return super(CuisineViewSet, self).dispatch(*args, **kwargs)

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
