from django import forms
from .models import Collection, Card, Deck


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'border rounded-lg p-2 w-full', 'placeholder': 'Collection name'}),
            'description': forms.Textarea(
                attrs={'class': 'border rounded-lg p-2 w-full', 'rows': 4, 'placeholder': 'Collection description'}),
        }


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['front', 'back']
        widgets = {
            'front': forms.Textarea(attrs={'class': 'border rounded-lg p-2 w-full', 'rows': 4,
                                           'placeholder': 'Front side of the card (question)'}),
            'back': forms.Textarea(attrs={'class': 'border rounded-lg p-2 w-full', 'rows': 4,
                                          'placeholder': 'Back side of the card (answer)'}),
        }


class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'border rounded-lg p-2 w-full', 'placeholder': 'Deck name'}),
            'description': forms.Textarea(
                attrs={'class': 'border rounded-lg p-2 w-full', 'rows': 4, 'placeholder': 'Deck description'}),
        }
