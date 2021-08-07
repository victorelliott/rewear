from django.contrib import admin

from .models import ClothingItem, ClothingWearDate, ClothingTag

# Register your models here.
admin.site.register(ClothingItem)
admin.site.register(ClothingWearDate)
admin.site.register(ClothingTag)