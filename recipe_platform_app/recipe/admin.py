from django.contrib import admin
from embed_video.admin import AdminVideoMixin

from .models import *


##giving admin more control over the recipe posts uploaded
class RecipeAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comment)
admin.site.register(Category)
