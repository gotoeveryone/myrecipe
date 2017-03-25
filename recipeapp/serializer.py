""" API用シリアライザ """
from rest_framework import serializers
from .models import Instruction, Quantity

class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = ('id', 'cuisine', 'sort_order', 'description')

class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quantity
        fields = ('id', 'cuisine_id', 'foodstuff', 'detail')
