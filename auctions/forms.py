from django import forms
from auctions.models import Item

class SearchForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('type','level')
        widgets = {
                    'type': forms.Select(attrs={'class': 'span12'}),
                    'level': forms.TextInput(attrs={'class': 'span4'})
        }