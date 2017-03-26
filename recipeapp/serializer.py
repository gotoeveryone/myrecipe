""" API用シリアライザ """
from rest_framework import serializers
from .models import Cuisine, Instruction, Quantity, Foodstuff

class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = ('id', 'sort_order', 'description')

class FoodstuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foodstuff
        fields = ('id', 'name', 'classification')

class QuantitySerializer(serializers.ModelSerializer):
    foodstuff = FoodstuffSerializer(read_only=True)
    class Meta:
        model = Quantity
        fields = ('id', 'cuisine_id', 'foodstuff', 'detail')

class CuisineSerializer(serializers.ModelSerializer):
    instructions = InstructionSerializer(many=True, read_only=True)
    quantities = QuantitySerializer(many=True, read_only=True)
    class Meta:
        model = Cuisine
        fields = ('id', 'name', 'classification', 'ingestion_kcal', 'create_number_of_times', 'instructions', 'quantities')
