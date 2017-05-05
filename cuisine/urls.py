""" URL """
from django.conf.urls import url, include
from rest_framework import routers
from . import views

urlpatterns = [
    url(r'^$', views.CuisineListView.as_view(), name='index'),
    url(r'^add/', views.cuisine_add, name='add'),
    url(r'^edit/(?P<pk>\d+)/', views.CuisineDetailView.as_view(), name='edit'),
]
