from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from .models import Product, ProductComment, ProductLike, ProductShare
from .serializers import ProductSerializer, ProductCommentSerializer, ProductLikeSerializer, ProductShareSerializer
import math

# -----------------------------
# Product Endpoints
# -----------------------------
class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(verified=True).order_by('-date_posted')


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
        queryset = Product.objects.filter(verified=True)
        lat = self.request.query_params.get("lat")
        lng = self.request.query_params.get("lng")
        radius = self.request.query_params.get("radius", 5)

        if not lat or not lng:
            raise ValidationError({"detail": "Latitude and longitude are required."})

        try:
            lat = float(lat)
            lng = float(lng)
            radius = float(radius)
        except ValueError:
            raise ValidationError({"detail": "Invalid latitude, longitude, or radius."})

        def haversine(lat1, lon1, lat2, lon2):
            R = 6371
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

        nearby = [
            p for p in queryset
            if p.latitude and p.longitude
            and haversine(lat, lng, float(p.latitude), float(p.longitude)) <= radius
        ]
        return nearby

# -----------------------------
# Comments
# -----------------------------
class ProductCommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductCommentSerializer

    def get_queryset(self):
        product_id = self.kwargs.get("pk")
        return ProductComment.objects.filter(product_id=product_id).order_by("-created_at")

    def perform_create(self, serializer):
        product_id = self.kwargs.get("pk")
        product = Product.objects.get(pk=product_id)
        serializer.save(product=product)


# -----------------------------
# Likes
# -----------------------------
class ProductLikeToggleAPIView(APIView):
    def post(self, request, pk):
        email = request.data.get("email")
        if not email:
            return Response({"error": "Email is required"}, status=400)

        product = Product.objects.get(pk=pk)
        like, created = ProductLike.objects.get_or_create(product=product, email=email)

        if not created:  # unlike if already liked
            like.delete()
            return Response({"message": "Unliked", "likes_count": product.like_count})

        return Response({"message": "Liked", "likes_count": product.like_count})


# -----------------------------
# Shares
# -----------------------------
class ProductShareCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductShareSerializer

    def perform_create(self, serializer):
        product_id = self.kwargs.get("pk")
        product = Product.objects.get(pk=product_id)
        serializer.save(product=product)
