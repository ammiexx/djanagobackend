from rest_framework import generics
from rest_framework import filters
from .models import PostProduct
from .serializers import ProductSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = PostProduct.objects.all()
    serializer_class = ProductSerializer


class ProductSearchView(generics.ListAPIView):
    queryset = PostProduct.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'payment'] 

class ProductRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = PostProduct.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' 

class ProdcutDestroyView(generics.DestroyAPIView):
    queryset = PostProduct.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'




