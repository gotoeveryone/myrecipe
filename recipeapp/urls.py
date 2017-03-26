""" URL """
from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'cuisine', views.CuisineViewSet)
router.register(r'instructions', views.InstructionViewSet)
router.register(r'quantities', views.QuantityViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^menu/$', views.menu, name='menu'),
    url(r'^cuisine/$', views.CuisineListView.as_view(), name='cuisine'),
    url(r'^cuisine/add/', views.cuisine_add, name='add_cuisine'),
    url(r'^cuisine/edit/(?P<pk>\d+)/', views.CuisineDetailView.as_view(), name='edit_cuisine'),

    # REST API
    url(r'^api/', include(router.urls)),
]
