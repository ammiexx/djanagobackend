from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Product
from .serializers import ProductSerializer
import math

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class MyProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('userId')
        if user_id:
            return Product.objects.filter(clerk_user_id=user_id)
        return Product.objects.none()

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class NearbyProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()

        # Read query params
        lat = self.request.query_params.get("lat")
        lng = self.request.query_params.get("lng")
        radius = self.request.query_params.get("radius", 5)  # default 5km

        if not lat or not lng:
            raise ValidationError({"detail": "Latitude and longitude are required."})

        try:
            lat = float(lat)
            lng = float(lng)
            radius = float(radius)
        except ValueError:
            raise ValidationError({"detail": "Invalid latitude, longitude, or radius."})

        # Haversine formula
        def haversine(lat1, lon1, lat2, lon2):
            R = 6371  # Earth radius in km
            dlat = math.radians(lat2 - lat1)
            dlon = math.radians(lon2 - lon1)
            a = (
                math.sin(dlat / 2) ** 2
                + math.cos(math.radians(lat1))
                * math.cos(math.radians(lat2))
                * math.sin(dlon / 2) ** 2
            )
            c = 2 * math.asin(math.sqrt(a))
            return R * c

        # Filter products
        nearby = [
            p for p in queryset
            if p.latitude and p.longitude
            and haversine(lat, lng, float(p.latitude), float(p.longitude)) <= radius
        ]

        return nearby