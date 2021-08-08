from django.contrib import admin

from .models import ClothingItem, ClothingWearDate, ClothingTag

# Register your models here.

@admin.register(ClothingItem)
class ClothingItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'display_tags')
    list_filter = ('tags',)
    search_fields = ['name']
    
@admin.register(ClothingWearDate)
class ClothingWearDateAdmin(admin.ModelAdmin):
    list_display = ('date', 'display_clothing_items')
    list_filter = ('date', 'clothing_items')
    
@admin.register(ClothingTag)
class ClothingTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ['name']