from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from .models import Card, Collection, Deck
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import CardForm, CollectionForm, DeckForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


def index(request):
    return render(request, "flashcards_app/index.html")


# ------------------ Collection Views -----------------
class CollectionListView(LoginRequiredMixin, ListView):
    model = Collection
    template_name = "flashcards_app/collections.html"
    form_class = CollectionForm
    context_object_name = "collections"

    def get_queryset(self):
        return Collection.objects.filter(owner=self.request.user)


class CollectionCreateView(LoginRequiredMixin, CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = "flashcards_app/collection_create.html"
    success_url = reverse_lazy("collection-list")

    def get_queryset(self):
        return Collection.objects.filter(owner=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CollectionUpdateView(LoginRequiredMixin, UpdateView):
    model = Collection
    fields = ['name', 'description']
    template_name = "flashcards_app/collection_update.html"

    def get_queryset(self):
        return Collection.objects.filter(owner=self.request.user)

    def get_success_url(self):
        return reverse_lazy("decks-by-collection", kwargs={"pk": self.kwargs['pk']})


class CollectionDeleteView(LoginRequiredMixin, DeleteView):
    model = Collection
    template_name = "flashcards_app/collection_delete.html"
    success_url = "/collections/"

    def get_queryset(self):
        return Collection.objects.filter(owner=self.request.user)


# ------------------ Card Views -----------------

class CardListView(LoginRequiredMixin, ListView):
    model = Card
    template_name = "flashcards_app/cards.html"
    context_object_name = "cards"
    paginate_by = 1

    def get_queryset(self):
        return Card.objects.filter(collection=self.kwargs['pk'], deck=self.kwargs['deck_pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deck'] = get_object_or_404(Deck, pk=self.kwargs['deck_pk'])
        return context


class CardReverseListView(LoginRequiredMixin, ListView):
    model = Card
    template_name = "flashcards_app/cards_reverse.html"
    context_object_name = "cards"
    paginate_by = 1

    def get_queryset(self):
        return Card.objects.filter(collection=self.kwargs['pk'], deck=self.kwargs['deck_pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deck'] = get_object_or_404(Deck, pk=self.kwargs['deck_pk'])
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
        next_url = self.request.POST.get('next') or self.request.GET.get('next')
        if next_url:
            return next_url

        return reverse_lazy("card-list", kwargs={
            "pk": self.kwargs['collection_pk'],
            "deck_pk": self.kwargs['deck_pk']
        })

    def get_object(self, queryset=None):
        return get_object_or_404(
            Card,
            pk=self.kwargs.get('card_pk'),
            collection__pk=self.kwargs.get('collection_pk'),
            deck__pk=self.kwargs.get('deck_pk')
        )


class CardDeleteView(DeleteView):
    model = Card
    template_name = "flashcards_app/card_delete.html"

    def get_object(self, queryset=None):
        return get_object_or_404(
            Card,
            pk=self.kwargs.get('card_pk'),
            collection__pk=self.kwargs.get('collection_pk'),
            deck__pk=self.kwargs.get('deck_pk')
        )

    def get_success_url(self):
        next_url = self.request.POST.get('next') or self.request.GET.get('next')

        if next_url:
            from urllib.parse import urlparse, parse_qs
            parsed_url = urlparse(next_url)
            query_params = parse_qs(parsed_url.query)
            current_page = query_params.get('page', [None])[0]

            if current_page:
                try:
                    current_page = int(current_page)
                    remaining_cards = Card.objects.filter(deck__pk=self.kwargs['deck_pk'])
                    paginator = Paginator(remaining_cards, 1)

                    if current_page > paginator.num_pages:
                        if paginator.num_pages > 0:
                            return f"{parsed_url.path}?page={paginator.num_pages}"
                        else:
                            return reverse_lazy("card-list", kwargs={
                                "pk": self.kwargs['collection_pk'],
                                "deck_pk": self.kwargs['deck_pk']
                            })
                    else:
                        return next_url
                except (ValueError, IndexError):
                    pass

        return reverse_lazy("card-list", kwargs={
            "pk": self.kwargs['collection_pk'],
            "deck_pk": self.kwargs['deck_pk']
        })


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
        collection_pk = self.kwargs.get('pk')
        collection = get_object_or_404(Collection, pk=collection_pk)

        queryset = Deck.objects.filter(collection=collection).annotate(card_count=Count('cards'))

        return queryset



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
        collection_pk = self.kwargs.get("pk")
        deck_pk = self.kwargs.get("deck_pk")

        return get_object_or_404(
            Deck,
            pk=deck_pk,
            collection__pk=collection_pk
        )


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
