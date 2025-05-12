from rest_framework import generics
from .models import SalesMan
from .serializers import SalesManSerializer

class SalesManListCreateView(generics.ListCreateAPIView):
    queryset = SalesMan.objects.all()
    serializer_class = SalesManSerializer


