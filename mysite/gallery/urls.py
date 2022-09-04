from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

##url and view for artwork detail
urlpatterns = [
    path('', views.index, name='index'),
    path('artworks/', views.ArtworkListView.as_view(), name='artworks'),
    path('artists', views.artists, name='artists'),
    path('shareart',views.Share_ArtView, name='shareart')

    # path('share_art/', views.share_art(), name='share_art')
]
