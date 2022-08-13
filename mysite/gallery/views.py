from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')
    """View function for home page of site."""

def artists(request):
    return render(request, 'artists.html')

    