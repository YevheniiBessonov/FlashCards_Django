from django.urls import path
from .views import CollectionListView, CollectionCreateView, CollectionDeleteView, \
    CollectionUpdateView, CardCreateView, DeckUpdateView, DeckDeleteView, DeckCreateView, DecksByCollection, \
    DeckListView, CardListView, CardUpdateView, CardDeleteView, CardReverseListView

urlpatterns = [
    path("collections/", CollectionListView.as_view(), name="collection-list"),
    path("collections/create/", CollectionCreateView.as_view(), name="collection-create"),
    path("collections/<int:pk>/delete/", CollectionDeleteView.as_view(), name="collection-delete"),
    path("collections/<int:pk>/update/", CollectionUpdateView.as_view(), name="collection-update"),
    path("collections/<int:pk>/create-card/", CardCreateView.as_view(), name="collection-create-card", ),
    path("collections/<int:pk>/deck_create/", DeckCreateView.as_view(), name="deck-create"),
    path("collections/<int:pk>/decks/", DecksByCollection.as_view(), name="decks-by-collection"),
    path("collections/<int:pk>/decks/<int:deck_pk>/", DeckListView.as_view(), name="deck-detail"),
    path("collections/<int:pk>/decks/<int:deck_pk>/delete", DeckDeleteView.as_view(), name="deck-delete"),
    path("collections/<int:pk>/decks/<int:deck_pk>/edit", DeckUpdateView.as_view(), name="deck-update"),
    path("collections/<int:pk>/decks/<int:deck_pk>/create-card", CardCreateView.as_view(), name="card-create"),
    path("collections/<int:pk>/decks/<int:deck_pk>/cards", CardListView.as_view(), name="card-list"),
    path("collections/<int:pk>/decks/<int:deck_pk>/cards_reverse", CardReverseListView.as_view(),
         name="card-reverse_list"),

    path("collections/<int:collection_pk>/decks/<int:deck_pk>/cards/<int:card_pk>/edit", CardUpdateView.as_view(),
         name="card-update"),
    path("collections/<int:collection_pk>/decks/<int:deck_pk>/cards/<int:card_pk>/delete", CardDeleteView.as_view(),
         name="card-delete"),

]
