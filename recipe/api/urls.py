""" URL """
from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'cuisine', views.CuisineViewSet)
router.register(r'instructions', views.InstructionViewSet)
router.register(r'quantities', views.QuantityViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
