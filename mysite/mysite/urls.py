"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# Use include() to add paths from the gallery application
from django.urls import include
from django.views.generic import RedirectView
from django.views.generic.edit import FormView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('gallery/', include('gallery.urls')),
]

#Add URL maps to redirect the base URL to our application
urlpatterns += [
    path('', RedirectView.as_view(url='gallery/', permanent=True)),
]

# Use static() to add URL mapping to serve static files during development (only)
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += [
#     path('artwork/create/',  views.ArtworkCreate.as_view(), name='artwork-create'),
# ]