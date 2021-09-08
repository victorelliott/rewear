from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(
        """Welcome to the index view. This is where the user will be able to
        view, sort, filter, and search their list of clothes."""
        )
    
def add(request):
    return HttpResponse(
        """Welcome to the add view. This is where new items of clothing 
        will be added to the user's list."""
        )

def log(request):
    return HttpResponse(
        """View for displaying the calendar and adding clothing items to dates."""
    )

def item(request, pk):
    return HttpResponse(
        "View for adding a new item to the wardrobe (" + str(pk) + ")."
    )

def edit(request, pk):
    return HttpResponse(
        "View for editing the details of a clothing item (" + str(pk) + ")."
    )

