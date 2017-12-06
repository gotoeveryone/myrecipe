""" URL """
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from recipe.cuisine.views import CuisineListView, notice

app_name = 'recipe_cuisine'

urlpatterns = [
    url(r'^$', login_required(CuisineListView.as_view()), name='index'),
    url(r'^notice/(?P<pk>\d+)/', login_required(notice), name='notice'),
]
