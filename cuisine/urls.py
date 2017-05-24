""" URL """
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import CuisineListView, CuisineAddView, CuisineDetailView

urlpatterns = [
    url(r'^$', login_required(CuisineListView.as_view()), name='index'),
    url(r'^add/', login_required(CuisineAddView.as_view()), name='add'),
    url(r'^edit/(?P<pk>\d+)/', login_required(CuisineDetailView.as_view()), name='edit'),
]
