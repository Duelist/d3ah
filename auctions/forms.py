from django import forms
from auctions.models import Item

class SearchForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('type','level')