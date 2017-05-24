"""recipe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import os
from django.conf.urls import include, url
from django.contrib import admin
from . import settings

PREFIX = os.environ.get('RECIPE_PREFIX', default='')
urlpatterns = [
    url(r'^' + PREFIX, include('recipe.core.urls', namespace='recipe')),
    url(r'^' + PREFIX + 'cuisine/', include('recipe.cuisine.urls', namespace='recipe_cuisine')),
    url(r'^' + PREFIX + 'api/', include('recipe.api.urls', namespace='recipe_api')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^' + PREFIX + '__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
