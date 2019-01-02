""" URL """
from django.urls import include, path
from rest_framework import routers
from recipe.api import views

router = routers.DefaultRouter()
router.register(r'cuisine', views.CuisineViewSet)
router.register(r'classifications', views.ClassificationViewSet)
router.register(r'foodstuffs', views.FoodstuffViewSet)

app_name = 'recipe_api'

urlpatterns = [
    path('', include(router.urls)),
    path('health', views.health, name='health'),
    path('user', views.user, name='user'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('notice', views.notice, name='notice'),
]
