from django import forms 

from tpopstore.models import Artist, Product

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('artist_name', 'image')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'category', 'artist', 'description', 'price', 'image', 'inventory')