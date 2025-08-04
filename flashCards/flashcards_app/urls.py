from django.contrib import admin
from django.urls import path, include
from .views import index, CollectionListView, CollectionDetailView, CollectionCreateView, CollectionDeleteView, \
    CollectionUpdateView

urlpatterns = [
    path("", index, name="index"),
    path("collections/", CollectionListView.as_view(), name="collection-list"),
    path("collections/<int:pk>/", CollectionDetailView.as_view(), name="collection-detail"),
    path("collections/create/", CollectionCreateView.as_view(), name="collection-create"),
    path("collections/<int:pk>/delete/", CollectionDeleteView.as_view(), name="collection-delete"),
    path("collections/<int:pk>/update/", CollectionUpdateView.as_view(), name="collection-update"),

]
