from django.db import models
from django.contrib.auth.models import User


class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="collections")

    class Meta:
        ordering = ['-created_at']


class Card(models.Model):
    front = models.TextField()
    back = models.TextField()
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name="cards")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
