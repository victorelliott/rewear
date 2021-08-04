from django.contrib import admin

from .models import ClothingItem, WearDate

# Register your models here.
admin.site.register(ClothingItem)
admin.site.register(WearDate)