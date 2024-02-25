from django.urls import path
from .views import ItemListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView

urlpatterns = [
    path("", ItemListView.as_view(), name="snack_list"),
    path("<int:pk>/", ItemDetailView.as_view(), name="snack_detail"),
    path("create/", ItemCreateView.as_view(), name="snack_create"),
    path("<int:pk>/update", ItemUpdateView.as_view(), name="snack_update"),
    path("<int:pk>/delete", ItemDeleteView.as_view(), name="snack_delete"),
]
