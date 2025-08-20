from django.urls import path
from .views import ProductListCreateAPIView

urlpatterns = [
    path('newproducts/', ProductListCreateAPIView.as_view(), name='product-list-create'),
]
