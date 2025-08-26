from django.urls import path
from .views import ProductListCreateAPIView,MyProductListAPIView,ProductRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('myproducts/',MyProductListAPIView.as_view(),name='my-product-list'),
    path('delete/products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),  # ✅ For GET, PATCH, DELETE
]
