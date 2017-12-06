""" URL """
from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'cuisine', views.CuisineViewSet)
router.register(r'foodstuffs', views.FoodstuffViewSet)

app_name = 'recipe_api'

urlpatterns = [
    url(r'^', include(router.urls)),
]
