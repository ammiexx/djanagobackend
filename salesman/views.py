from rest_framework import generics
from rest_framework import filters
from .models import SalesMan
from .serializers import SalesManSerializer

class SalesManListCreateView(generics.ListCreateAPIView):
    queryset = SalesMan.objects.all()
    serializer_class = SalesManSerializer

class SalesManSearchView(generics.ListAPIView):
    queryset = SalesMan.objects.all()
    serializer_class = SalesManSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['fname', 'lname','email'] 

class SalesManRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = SalesMan.objects.all()
    serializer_class = SalesManSerializer
    lookup_field = 'pk' 

class SalesManDestroyView(generics.DestroyAPIView):
    queryset =SalesMan.objects.all()
    serializer_class = SalesManSerializer
    lookup_field = 'pk'