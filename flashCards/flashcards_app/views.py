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
    success_url = "/collection/"


class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = "flashcards_app/collection_delete.html"
    success_url = "/collections/"


# ------------------ Card Views -----------------

class CardListView(ListView):
    model = Card
    template_name = "flashcards_app/cards.html"
    context_object_name = "cards"


class CardDetailView(DetailView):
    model = Card
    template_name = "flashcards_app/collections.html"
    context_object_name = "card"


class CardCreateView(CreateView):
    model = Card
    form_class = CardForm
    template_name = "flashcards_app/card_create.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        self.collection = get_object_or_404(Collection, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.collection = self.collection
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collection'] = self.collection
        return context

    def get_success_url(self):
        return reverse_lazy("collection-detail", kwargs={"pk": self.collection.pk})


# ------------------ Deck Views -----------------

class DeckListView(ListView):
    model = Deck
    template_name = "flashcards_app/decks.html"
    context_object_name = "decks"


class DeckDetailView(DetailView):
    model = Deck
    template_name = "flashcards_app/decks.html"
    context_object_name = "decks"


class DeckCreateView(CreateView):
    model = Deck
    form_class = DeckForm
    template_name = "flashcards_app/deck_create.html"
    success_url = reverse_lazy("deck-list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.collection = get_object_or_404(Collection, pk=self.kwargs['pk'])
        return super().form_valid(form)


class DeckUpdateView(UpdateView):
    model = Deck
    fields = ['name', 'description']
    template_name = "flashcards_app/deck_update.html"
    success_url = "/collections/"


class DeckDeleteView(DeleteView):
    model = Deck
    template_name = "flashcards_app/deck_delete.html"
    success_url = "/collections/"
