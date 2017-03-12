""" URL """
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^menu/$', views.menu, name='menu'),
    url(r'^cuisine/$', views.cuisine, name='cuisine'),
    url(r'^cuisine/search/$', views.cuisine_search, name='search_cuisine'),
    url(r'^cuisine/edit/(?P<primary_key>\d+)/', views.cuisine_edit, name='edit_cuisine'),
]
