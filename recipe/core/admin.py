from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from recipe.core.models import User, Cuisine, Classification, Instruction, Foodstuff

admin.site.register(Cuisine)
admin.site.register(Classification)
admin.site.register(Instruction)
admin.site.register(Foodstuff)


@admin.register(User)
class AdminUserAdmin(UserAdmin):
    """ ユーザ管理 """
