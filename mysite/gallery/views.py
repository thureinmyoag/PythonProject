from django.shortcuts import render
## django import models
# Create your views here.
from .models import Artwork,Artist,Genre
def index(request):
    return render(request, 'index.html')
    """View function for home page of site."""

def artists(request):
    return render(request, 'artists.html')

def share_art(request):
    return render(request,'share_art.html')

# def share_art(request):
#     return render(request, 'share_art.html')

from django.views import generic

class ArtworkListView(generic.ListView):
    model = Artwork
    context_object_name = 'artwork_list'   # your own name for the list as a template variable
    queryset = Artwork.objects.all() # Get 5 books
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ArtworkListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

def artwork_detail_view(request, primary_key):
    # book = get_object_or_404(Book, pk=primary_key)
    artwork = Artwork.objects.get(pk=primary_key)
    return render(request, 'gallery/artwork_detail.html', context={'artwork': artwork })

def Share_ArtView(request):
    return render(request,'gallery/share_art.html');