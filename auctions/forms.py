from django import forms
from mongodbforms import EmbeddedDocumentForm
from auctions.models import Item, ITEM_TYPES

class SearchForm(forms.Form):
    type = forms.ChoiceField(choices=ITEM_TYPES,
                             required=True,
                             widget=forms.Select(attrs={'class': 'span12'}))
    level = forms.IntegerField(min_value=1,
                               max_value=80,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'span12'}))