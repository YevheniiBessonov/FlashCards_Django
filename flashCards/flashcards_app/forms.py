from django import forms
from .models import Collection, Card


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border rounded-lg p-2 w-full', 'placeholder': 'Название коллекции'}),
            'description': forms.Textarea(attrs={'class': 'border rounded-lg p-2 w-full', 'rows': 4, 'placeholder': 'Описание коллекции'}),
        }


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['front', 'back']
        widgets = {
            'front': forms.Textarea(attrs={'class': 'border rounded-lg p-2 w-full', 'rows': 4, 'placeholder': 'Лицевая сторона карточки (вопрос)'}),
            'back': forms.Textarea(attrs={'class': 'border rounded-lg p-2 w-full', 'rows': 4, 'placeholder': 'Обратная сторона карточки (ответ)'}),
        }