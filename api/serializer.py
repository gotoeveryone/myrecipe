""" API用シリアライザ """
from rest_framework import serializers
from common.models import Cuisine, Instruction, Quantity, Foodstuff

class InstructionSerializer(serializers.ModelSerializer):
    """ 調理手順モデルのシリアライザ """
    class Meta:
        model = Instruction
        fields = ('id', 'sort_order', 'description')
        extra_kwargs = {'id': {'read_only': False}}

class FoodstuffSerializer(serializers.ModelSerializer):
    """ 食材モデルのシリアライザ """
    class Meta:
        model = Foodstuff
        fields = ('id', 'name', 'classification')

class QuantitySerializer(serializers.ModelSerializer):
    """ 分量モデルのシリアライザ """
    foodstuff = FoodstuffSerializer(read_only=True)
    class Meta:
        model = Quantity
        fields = ('id', 'cuisine_id', 'foodstuff', 'detail')
        extra_kwargs = {'id': {'read_only': False}}

class CuisineSerializer(serializers.ModelSerializer):
    """ メニューモデルのシリアライザ """
    instructions = InstructionSerializer(many=True, read_only=False)
    quantities = QuantitySerializer(many=True, read_only=False)

    def update(self, instance: Cuisine, validated_data):
        # 調理手順を更新
        instructions_data = validated_data.pop('instructions')
        for instruction in instructions_data:
            data = Instruction.objects.filter(id=instruction['id']).first()
            data.description = instruction['description']
            data.sort_order = instruction['sort_order']
            data.save()

        # 分量を更新
        quantities_data = validated_data.pop('quantities')
        for quantity in quantities_data:
            data = Quantity.objects.filter(id=quantity['id']).first()
            data.detail = quantity['detail']
            data.save()

        return super().update(instance, validated_data)

    class Meta:
        model = Cuisine
        fields = ('id', 'name', 'classification', 'ingestion_kcal',\
            'create_number_of_times', 'instructions', 'quantities')
