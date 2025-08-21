from django.urls import path
from .views import ProductListCreateAPIView

urlpatterns = [
    path('maintenance/', ProductListCreateAPIView.as_view(), name='product-list-create'),
]
