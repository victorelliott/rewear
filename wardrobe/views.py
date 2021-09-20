from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import ClothingItem
from .forms import ClothingItemForm

# Create your views here.
def index(request):
    item_list = ClothingItem.objects.all()
    context = {'item_list': item_list}
    return render(request, 'wardrobe/index.html', context)
    
def add(request):
    if request.method == 'POST':
        form = ClothingItemForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save()
            return redirect(new_item)
    else:
        form = ClothingItemForm()
    context = {'form': form}
    return render(request, 'wardrobe/add.html', context)

def log(request):
    return render(request, 'wardrobe/log.html')

def item(request, item_id):
    item = get_object_or_404(ClothingItem, id=item_id)
    context = {'item': item}
    return render(request, 'wardrobe/item.html', context)

def edit(request, item_id):
    return render(request, 'wardrobe/edit.html')