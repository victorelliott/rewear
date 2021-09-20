from django import forms

from .models import ClothingItem

class ClothingItemForm(forms.ModelForm):
    class Meta:
        model = ClothingItem
        fields = ['name', 'picture', 'price', 'description', 'tags']

