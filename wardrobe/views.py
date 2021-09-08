from django.shortcuts import render

from .models import ClothingItem

# Create your views here.
def index(request):
    item_list = ClothingItem.objects.all()
    context = {'item_list': item_list}
    return render(request, 'wardrobe/index.html', context)
    
def add(request):
    return render(request, 'wardrobe/add.html')

def log(request):
    return render(request, 'wardrobe/log.html')

def item(request, pk):
    return render(request, 'wardrobe/item.html')

def edit(request, pk):
    return render(request, 'wardrobe/edit.html')