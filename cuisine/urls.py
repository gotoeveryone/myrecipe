from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='cuisine'),
    url(r'^search/$', views.search, name='search_cuisine'),
    url(r'^edit/(?P<id>\d+)/', views.edit, name='edit_cuisine'),
]
