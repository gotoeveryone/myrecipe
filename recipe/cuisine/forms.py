""" フォーム """
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from recipe.core.models import Cuisine, Instruction, Quantity, Foodstuff

class CuisineForm(forms.ModelForm):
    """ 料理フォーム """
    name = forms.CharField(required=False, max_length=255)
    classification = forms.ChoiceField(required=False,
        choices=(('', ''), ('主菜', '主菜'), ('主食', '主食'), ('副菜', '副菜'), ('デザート', 'デザート')))
    ingestion_kcal = forms.CharField(required=False)
    create_number_of_times = forms.CharField(required=False)

    class Meta:
        model = Cuisine
        fields = ['name', 'classification', 'ingestion_kcal', 'create_number_of_times']
