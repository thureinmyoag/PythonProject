from django.contrib import admin

# Register your models here.
from .models import Genre,Artwork,Artist

admin.site.register(Genre)
admin.site.register(Artwork)
admin.site.register(Artist)