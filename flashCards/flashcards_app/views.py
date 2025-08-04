from django.shortcuts import render, HttpResponse
from .models import Card, Collection
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CardForm, CollectionForm
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
    template_name = "flashcards_app/collection_detail.html"
    context_object_name = "collection"


class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = "flashcards_app/collection_create.html"
    success_url = reverse_lazy("collection-list")


    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    # add the user's collections to the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["collections"] = Collection.objects.filter(owner=self.request.user)
        return context

class CollectionUpdateView(UpdateView):
    model = Collection
    fields = ['name', 'description']
    template_name = "flashcards_app/collection_update.html"
    success_url = "/collection/"


class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = "flashcards_app/collection_delete.html"
    success_url = "/collection/"

# ------------------ Card Views -----------------
