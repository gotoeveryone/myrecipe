""" フォーム """
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from recipe.models import Cuisine, Instruction, Quantity, Foodstuff

class CuisineForm(forms.ModelForm):
    """ 料理フォーム """
    name = forms.CharField(required=False, max_length=255)
    classification = forms.ChoiceField(required=False,
        choices=(('', ''), ('1', '主菜'), ('2', '主食'), ('3', '副菜'), ('4', 'デザート')))
    ingestion_kcal = forms.CharField(required=False)
    create_number_of_times = forms.CharField(required=False)
    instructions = forms.ModelMultipleChoiceField(queryset=Instruction.objects.all())

    # def __str__(self):
    #     return self.name

    class Meta:
        model = Cuisine
        fields = ['name', 'classification', 'ingestion_kcal', 'create_number_of_times']

    # def __init__(self, *args, **kwargs):
    #     super(CuisineForm, self).__init__(*args, **kwargs)
    #     print(self.fields)
    # #     self.fields['instructions'] = forms.ModelChoiceField(queryset=Instruction.objects.all().order_by('sort_order'))
    #     self.fields['quantities'] = forms.ModelChoiceField(queryset=Quantity.objects.all())

class InstructionForm(forms.ModelForm):
    """ 調理手順 """
    sort_order = forms.IntegerField('並び順',\
        validators=[MinValueValidator(1), MaxValueValidator(3)])
    description = forms.CharField(max_length=255)
    cuisine = forms.ModelChoiceField(Cuisine)

    def __str__(self):
        return self.description

    class Meta:
        model = Instruction
        fields = ['sort_order', 'description', 'cuisine']

class QuantityForm(forms.ModelForm):
    """ 調理手順 """
    sort_order = forms.IntegerField('並び順',\
        validators=[MinValueValidator(1), MaxValueValidator(3)])
    description = forms.CharField(max_length=255)

    def __str__(self):
        return self.description

    class Meta:
        model = Quantity
        fields = []

class FoodstuffForm(forms.ModelForm):
    """ 食材 """
    name = forms.CharField(max_length=255)
    classification = forms.CharField(max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        model = Foodstuff
        fields = []

class EditCuisineForm(forms.ModelForm):
    """ Edit Cuisine Form """

    class Meta:
        model = Cuisine
        fields = ['id', 'name']
