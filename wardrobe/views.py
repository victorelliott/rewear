from django.shortcuts import render, get_object_or_404

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

def item(request, item_id):
    item = get_object_or_404(ClothingItem, id=item_id)
    context = {'item': item}
    return render(request, 'wardrobe/item.html', context)

def edit(request, item_id):
    return render(request, 'wardrobe/edit.html')