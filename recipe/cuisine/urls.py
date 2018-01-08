""" URL """
from django.urls import path
from django.contrib.auth.decorators import login_required
from recipe.cuisine.views import CuisineListView, notice

app_name = 'recipe_cuisine'

urlpatterns = [
    path('', login_required(CuisineListView.as_view()), name='index'),
    path('notice/<int:key>/', login_required(notice), name='notice'),
]
