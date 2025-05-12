from rest_framework import generics
from .models import PostProduct
from .serializers import JobSerializer


class JobListCreateView(generics.ListCreateAPIView):
    queryset = PostProduct.objects.all()
    serializer_class = JobSerializer