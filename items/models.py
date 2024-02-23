
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse



class Item(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField(default="", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("item_detail", args=[str(self.id)])
