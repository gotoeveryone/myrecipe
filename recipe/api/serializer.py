""" API用シリアライザ """
from rest_framework import serializers, fields
from recipe.core.models import Cuisine, Instruction, Foodstuff

class InstructionSerializer(serializers.ModelSerializer):
    """ 調理手順 """
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Instruction
        fields = ('id', 'sort_order', 'description')

class FoodstuffSerializer(serializers.ModelSerializer):
    """ 食材 """
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Foodstuff
        fields = ('id', 'name', 'quantity')

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

    def save_instruction(self, instance, input_data):
        """ 調理手順の保存 """
        if 'id' in input_data:
            instruction = Instruction.objects.filter(id=input_data['id']).first()
            instruction.description = input_data['description']
            instruction.sort_order = input_data['sort_order']
        else:
            instruction = Instruction(
                cuisine=instance,
                description=input_data['description'],
                sort_order=input_data['sort_order'],
            )

        instruction.created_by = instance.created_by
        instruction.modified_by = instance.modified_by
        return instruction.save()

    def save_foodstuff(self, instance, input_data):
        """ 食材の保存 """
        if 'id' in input_data:
            foodstuff = Foodstuff.objects.filter(id=input_data['id']).first()
            foodstuff.name = input_data['name']
            foodstuff.detail = input_data['quantity']
        else:
            foodstuff = Foodstuff(
                cuisine=instance,
                name=input_data['name'],
                quantity=input_data['quantity'],
            )

        foodstuff.created_by = instance.created_by
        foodstuff.modified_by = instance.modified_by
        return foodstuff.save()

    def create(self, validated_data):
        instructions_data = validated_data.pop('instructions')
        foodstuffs_data = validated_data.pop('foodstuffs')
        cuisine = super().create(validated_data)

        # 調理手順を登録
        for instruction in instructions_data:
            self.save_instruction(cuisine, instruction)

        # 食材を登録
        for foodstuff in foodstuffs_data:
            self.save_foodstuff(cuisine, foodstuff)

        return cuisine

    def update(self, instance: Cuisine, validated_data):
        # 調理手順を更新
        instructions_data = validated_data.pop('instructions')
        for instruction in instructions_data:
            self.save_instruction(instance, instruction)

        # 食材を更新
        foodstuffs_data = validated_data.pop('foodstuffs')
        for foodstuff in foodstuffs_data:
            self.save_foodstuff(instance, foodstuff)

        return super().update(instance, validated_data)

    class Meta:
        model = Cuisine
        fields = ('id', 'name', 'classification', 'ingestion_kcal',\
            'create_number_of_times', 'instructions', 'foodstuffs', 'created_by', 'modified_by')
