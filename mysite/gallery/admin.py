from django.contrib import admin

# Register your models here.
from .models import Genre,Arts,Artist

admin.site.register(Genre)
admin.site.register(Arts)
admin.site.register(Artist)