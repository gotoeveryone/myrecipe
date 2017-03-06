from django.db import models
from django import forms

# Create your models here.
class Cuisine(models.Model):
    name = models.CharField(max_length=255)
    classification = models.CharField(max_length=5)
    ingestion_kcal = models.IntegerField(max_length=4)
    create_number_of_times = models.IntegerField(max_length=3)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cuisine'

# Create your models here.
class CuisineForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control text-box single-line'}))
    classification = forms.ChoiceField(required=False, choices=(('', ''), ('1', '主菜'), ('2', '主食'), ('3', '副菜'), ('4', 'デザート')))
    ingestion_kcal = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control text-box single-line'}))

    def __str__(self):
        return self.name
