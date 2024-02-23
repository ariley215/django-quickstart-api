from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Item
from .serializers import ItemSerializer
from .permissions import IsOwnerOrReadOnly

class ItemList(ListAPIView):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer
  permissions_classes = (IsOwnerOrReadOnly,)
  
class ItemDetail(RetrieveUpdateDestroyAPIView):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer
  permissions_classes = (IsOwnerOrReadOnly,)


