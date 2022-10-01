from django.shortcuts import render
from .models import Artwork,Artist,Genre
from django.views import generic
from django.http import HttpResponseRedirect, request

# Create your views here.
# from django.shortcuts import render
from .forms import ShareArtForm
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html')
    """View function for home page of site."""

def artists(request):
    return render(request, 'artists.html')

class ArtworkListView(generic.ListView):
    model = Artwork
    context_object_name = 'artwork_list'   # your own name for the list as a template variable
    queryset = Artwork.objects.all() 
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
    if request.method == "POST":
        form = ShareArtForm(request.POST,request.FILES)
        if form.is_valid():
            # return HttpResponseRedirect("/artworks")
            Artwork = form.save()
    else:
        form = ShareArtForm()     
    return render(request,'gallery/share_art.html', {"form": form});



