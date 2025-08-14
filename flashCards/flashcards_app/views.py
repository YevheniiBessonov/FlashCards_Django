from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Card, Collection, Deck
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CardForm, CollectionForm, DeckForm
from django.urls import reverse_lazy


def index(request):
    return render(request, "flashcards_app/index.html")


# ------------------ Collection Views -----------------
class CollectionListView(ListView):
    model = Collection
    template_name = "flashcards_app/collections.html"
    form_class = CollectionForm
    context_object_name = "collections"


class CollectionDetailView(DetailView):
    model = Collection
    template_name = "flashcards_app/collections.html"
    context_object_name = "collection"


class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = "flashcards_app/collection_create.html"
    success_url = reverse_lazy("collection-list")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CollectionUpdateView(UpdateView):
    model = Collection
    fields = ['name', 'description']
    template_name = "flashcards_app/collection_update.html"

    def get_success_url(self):
        return reverse_lazy("decks-by-collection", kwargs={"pk": self.kwargs['pk']})


class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = "flashcards_app/collection_delete.html"
    success_url = "/collections/"


# ------------------ Card Views -----------------

class CardListView(ListView):
    model = Card
    template_name = "flashcards_app/cards.html"
    context_object_name = "cards"
    paginate_by = 1

    def get_queryset(self):
        return Card.objects.filter(collection=self.kwargs['pk'], deck=self.kwargs['deck_pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deck'] = get_object_or_404(Deck, pk=self.kwargs['deck_pk'])
        context['collection'] = get_object_or_404(Collection, pk=self.kwargs['pk'])
        return context


class CardCreateView(CreateView):
    model = Card
    form_class = CardForm
    template_name = "flashcards_app/card_create.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.collection = get_object_or_404(Collection, pk=self.kwargs['pk'])
        form.instance.deck = get_object_or_404(
            Deck,
            pk=self.kwargs['deck_pk'],
            collection__pk=self.kwargs['pk']
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deck'] = get_object_or_404(Deck, pk=self.kwargs['deck_pk'])
        return context

    # def get_object(self, queryset=None):
    #     collection_pk = self.kwargs.get('pk')
    #     deck_pk = self.kwargs.get('deck_pk')
    #
    #     deck = get_object_or_404(Deck, pk=deck_pk, collection__pk=collection_pk)
    #     return deck

    def get_success_url(self):
        return reverse_lazy(
            "card-create",
            kwargs={
                "pk": self.kwargs["pk"],
                "deck_pk": self.kwargs["deck_pk"],
            }
        )


class CardUpdateView(UpdateView):
    model = Card
    form_class = CardForm
    template_name = "flashcards_app/card_update.html"

    def get_success_url(self):
        return reverse_lazy("card-list", kwargs={"pk": self.kwargs['collection_pk'], "deck_pk": self.kwargs['deck_pk']})

    def get_object(self, queryset=None):
        collection_pk = self.kwargs.get('collection_pk')
        deck_pk = self.kwargs.get('deck_pk')
        card_pk = self.kwargs.get('card_pk')

        card = get_object_or_404(
            Card,
            pk=card_pk,
            collection__pk=collection_pk,
            deck__pk=deck_pk
        )
        return card


class CardDeleteView(DeleteView):
    model = Card
    template_name = "flashcards_app/card_delete.html"

    def get_object(self, queryset=None):
        collection_pk = self.kwargs.get('collection_pk')
        deck_pk = self.kwargs.get('deck_pk')
        card_pk = self.kwargs.get('card_pk')

        card = get_object_or_404(
            Card,
            pk=card_pk,
            collection__pk=collection_pk,
            deck__pk=deck_pk
        )
        return card

    def get_success_url(self):
        return reverse_lazy("card-list", kwargs={"pk": self.kwargs['collection_pk'], "deck_pk": self.kwargs['deck_pk']})


# ------------------ Deck Views -----------------

class DeckListView(ListView):
    model = Deck
    template_name = "flashcards_app/decks.html"
    context_object_name = "decks"

    def get_object(self, queryset=None):
        collection_pk = self.kwargs.get('pk')
        deck_pk = self.kwargs.get('deck_pk')

        deck = get_object_or_404(Deck, pk=deck_pk, collection__pk=collection_pk)
        return deck


class DecksByCollection(ListView):
    model = Deck
    template_name = "flashcards_app/decks.html"
    context_object_name = "decks"

    def get_queryset(self):
        return Deck.objects.filter(collection_id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collection'] = get_object_or_404(Collection, pk=self.kwargs['pk'])
        return context


class DeckDetailView(DetailView):
    model = Deck
    template_name = "flashcards_app/decks.html"
    context_object_name = "decks"

    def get_object(self, queryset=None):
        collection_pk = self.kwargs.get('pk')
        deck_pk = self.kwargs.get('deck_pk')

        deck = get_object_or_404(Deck, pk=deck_pk, collection__pk=collection_pk)
        return deck


class DeckCreateView(CreateView):
    model = Deck
    form_class = DeckForm
    template_name = "flashcards_app/deck_create.html"

    def get_success_url(self):
        return reverse_lazy("decks-by-collection", kwargs={"pk": self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.collection = get_object_or_404(Collection, pk=self.kwargs['pk'])
        return super().form_valid(form)


class DeckUpdateView(UpdateView):
    model = Deck
    form_class = DeckForm
    template_name = "flashcards_app/deck_update.html"

    def get_success_url(self):
        return reverse_lazy("decks-by-collection", kwargs={"pk": self.kwargs['pk']})

    def get_object(self, queryset=None):
        collection_pk = self.kwargs.get('pk')
        deck_pk = self.kwargs.get('deck_pk')

        deck = get_object_or_404(Deck, pk=deck_pk, collection__pk=collection_pk)
        return deck


class DeckDeleteView(DeleteView):
    model = Deck
    template_name = "flashcards_app/deck_delete.html"

    def get_success_url(self):
        return reverse_lazy("decks-by-collection", kwargs={"pk": self.kwargs['pk']})

    def get_object(self, queryset=None):
        collection_pk = self.kwargs.get('pk')
        deck_pk = self.kwargs.get('deck_pk')

        deck = get_object_or_404(Deck, pk=deck_pk, collection__pk=collection_pk)
        return deck

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collection'] = get_object_or_404(Collection, pk=self.kwargs['pk'])
        return context
