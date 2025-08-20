from rest_framework import generics
from .models import RealEstate
from .serializers import RealEstateSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = RealEstate.objects.all()
    serializer_class = RealEstateSerializer
