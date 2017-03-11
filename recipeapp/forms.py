from django import forms

# Create your models here.
class CuisineForm(forms.Form):
    name = forms.CharField(required=False,\
        max_length=255, widget=forms.TextInput(\
            attrs={'class': 'form-control text-box single-line'}))
    classification = forms.ChoiceField(required=False,\
        choices=(('', ''), ('1', '主菜'), ('2', '主食'), ('3', '副菜'), ('4', 'デザート')))
    ingestion_kcal = forms.IntegerField(required=False,#
        widget=forms.TextInput(\
            attrs={'class': 'form-control text-box single-line'}))

    def __str__(self):
        return self.name
