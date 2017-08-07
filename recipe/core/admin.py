from django.contrib import admin
from recipe.core.models import Cuisine, Instruction, Foodstuff

admin.site.register(Cuisine)
admin.site.register(Instruction)
admin.site.register(Foodstuff)
