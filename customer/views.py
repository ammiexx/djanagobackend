from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer
class CustomerCListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer




