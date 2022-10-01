from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.forms.models import ModelForm

# Create your models here.
class Genre(models.Model):
    """Model representing a artwork genre."""
    name = models.CharField(max_length=100, help_text='Enter an arts genre (e.g. painting)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Artwork(models.Model):
    """Model representing a artwork (but not a specific copy of a artwork)."""
    title = models.CharField(max_length=100)
    
    # Foreign Key used because artwork can only have one author, but artists can have multiple artworks
    # Author as a string rather than object because it hasn't been declared yet in the file
    artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the artwork')
    image = models.ImageField(upload_to='images/', max_length=100)

    # ManyToManyField used because genre contain many artworks. artworks can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this artwork')

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this artwork."""
        return reverse('artwork-detail', args=[str(self.id)])

class Artist(models.Model):
    """Model representing an artist."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('artist-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

# class ShareArtForm(ModelForm):
#     class Meta:
#         model = Artwork
#         fields = ('title','artist','image','summary','genre')


