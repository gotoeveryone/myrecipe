""" API用シリアライザ """
from rest_framework import serializers, fields
from recipe.core.models import Cuisine, Instruction, Foodstuff

class InstructionSerializer(serializers.ModelSerializer):
    """ 調理手順 """
    class Meta:
        model = Instruction
        fields = ('sort_order', 'description')
        extra_kwargs = {'id': {'read_only': False}}

class FoodstuffSerializer(serializers.ModelSerializer):
    """ 食材 """
    class Meta:
        model = Foodstuff
        fields = ('name', 'quantity')
        extra_kwargs = {'id': {'read_only': False}}

class FoodstuffListSerializer(serializers.ModelSerializer):
    """ 食材一覧 """
    class Meta:
        model = Foodstuff
        fields = ('name',)

class CuisineListSerializer(serializers.ModelSerializer):
    """ レシピ一覧  """
    class Meta:
        model = Cuisine
        fields = ('id', 'name', 'classification', 'ingestion_kcal', 'create_number_of_times')

class CuisineSerializer(serializers.ModelSerializer):
    """ レシピ詳細 """
    instructions = InstructionSerializer(many=True, read_only=False)
    foodstuffs = FoodstuffSerializer(many=True, read_only=False)

    def update(self, instance: Cuisine, validated_data):
        # 調理手順を更新
        instructions_data = validated_data.pop('instructions')
        for instruction in instructions_data:
            data = Instruction.objects.filter(id=instruction['id']).first()
            data.description = instruction['description']
            data.sort_order = instruction['sort_order']
            data.save()

        # 分量を更新
        quantities_data = validated_data.pop('foodstuffs')
        for quantity in quantities_data:
            data = Foodstuff.objects.filter(id=quantity['id']).first()
            data.detail = quantity['detail']
            data.save()

        return super().update(instance, validated_data)

    class Meta:
        model = Cuisine
        fields = ('id', 'name', 'classification', 'ingestion_kcal',\
            'create_number_of_times', 'instructions', 'foodstuffs')
        extra_kwargs = {'id': {'read_only': False, 'required': True}}
