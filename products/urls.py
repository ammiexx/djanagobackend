from django.urls import path
from .views import ProductListCreateAPIView,MyProductListAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('myproducts/',MyProductListAPIView.as_view(),name='my-product-list'),
]
