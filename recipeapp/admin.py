from django.contrib import admin

# Register your models here.

from .models import Cuisine
from .models import Foodstuff

admin.site.register(Cuisine)
admin.site.register(Foodstuff)
