""" フォーム """
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from common.models import Cuisine, Instruction, Quantity, Foodstuff

class CuisineForm(forms.ModelForm):
    """ 料理フォーム """
    name = forms.CharField(required=False, max_length=255)
    classification = forms.ChoiceField(required=False,
        choices=(('', ''), ('1', '主菜'), ('2', '主食'), ('3', '副菜'), ('4', 'デザート')))
    ingestion_kcal = forms.CharField(required=False)
    create_number_of_times = forms.CharField(required=False)
    instructions = forms.ModelMultipleChoiceField(queryset=Instruction.objects.all())

    class Meta:
        model = Cuisine
        fields = ['name', 'classification', 'ingestion_kcal', 'create_number_of_times']
