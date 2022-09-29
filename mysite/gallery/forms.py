from django import forms
from django.forms.fields import CharField
from .models import Artwork
from django.forms.models import ModelForm

class ShareArtForm(ModelForm):
     # title = forms.CharField()
     # artist = forms.CheckboxSelectMultiple()
     # # genre = forms.Select()
     # image = forms.FileInput()
     # summary = forms.CharField(
     #      required = True,
     #      widget = forms.widgets.Textarea(
     #           attrs = {
     #                'class': 'form-control',
     #                "placeholder": "something",
     #           }
     #      ),
     #      label="Summary"
     #      )
     class Meta:
          model = Artwork
          fields = ('title','artist','image','summary','genre')
          widgets = {
               'title': forms.TextInput(attrs={'class': 'form-control '}),
               'artist': forms.TextInput(attrs={'class': 'form-control '}),
               'image': forms.FileInput(attrs={'class': 'form-control-file'}),
               'summary': forms.Textarea(attrs={'class': 'form-control '}),
               'genre': forms.Select(attrs={'class': 'form-control '}),
          }


