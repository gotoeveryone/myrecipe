""" フォーム """
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from recipe.core.models import Cuisine, Instruction, Quantity, Foodstuff

class LoginForm(forms.Form):
    """ ログインフォーム """
    account = forms.CharField(label='ID', max_length=20)
    password = forms.CharField(label='パスワード', max_length=40,\
        widget=forms.PasswordInput)
