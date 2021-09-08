from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'wardrobe/index.html')
    
def add(request):
    return render(request, 'wardrobe/add.html')

def log(request):
    return render(request, 'wardrobe/log.html')

def item(request, pk):
    return render(request, 'wardrobe/item.html')

def edit(request, pk):
    return render(request, 'wardrobe/edit.html')