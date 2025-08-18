from django import forms
from .models import Collection, Card, Deck

base_attrs = (
    "block w-full text-gray-700 rounded-lg px-3 py-2 my-2 "
    "border-none outline-none border-2 bg-gray-300 focus:bg-gray-100"
)


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ["name", "description"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": base_attrs, "placeholder": "Collection name"}
        )
        self.fields["description"].widget.attrs.update(
            {
                "class": base_attrs,
                "rows": 4,
                "placeholder": "Collection description",
            }
        )


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ["front", "back"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["front"].widget.attrs.update(
            {
                "class": base_attrs,
                "rows": 4,
                "placeholder": "Front side of the card (question)",
            }
        )
        self.fields["back"].widget.attrs.update(
            {
                "class": base_attrs,
                "rows": 4,
                "placeholder": "Back side of the card (answer)",
            }
        )


class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ["name", "description"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": base_attrs, "placeholder": "Deck name"}
        )
        self.fields["description"].widget.attrs.update(
            {
                "class": base_attrs,
                "rows": 4,
                "placeholder": "Deck description",
            }
        )
