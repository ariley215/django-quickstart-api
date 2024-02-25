from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Item

class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = "item_list.html"
    context_object_name = "items"
    
class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = "item_detail.html"
    
    
class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = "item_create.html"
    fields = "__all__"
    
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    template_name = "item_update.html"
    fields = ["name", "description"]

class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = "item_delete.html"
    success_url = reverse_lazy("item_list")
    