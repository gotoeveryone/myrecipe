""" URL """
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'cuisine', views.CuisineViewSet)
router.register(r'foodstuffs', views.FoodstuffViewSet)

app_name = 'recipe_api'

urlpatterns = [
    path('', include(router.urls)),
]
