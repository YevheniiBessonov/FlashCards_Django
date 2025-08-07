from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="collections")

    class Meta:
        ordering = ['-created_at']


class Deck(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="decks")
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name="decks")

    class Meta:
        ordering = ['-created_at']


class Card(models.Model):
    front = models.TextField(blank=True, null=True)
    back = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name="cards")
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name="cards")

    class Meta:
        ordering = ['-created_at']
