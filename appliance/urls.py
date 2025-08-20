from django.urls import path
from .views import ProductListCreateAPIView

urlpatterns = [
    path('appliances/', ProductListCreateAPIView.as_view(), name='product-list-create'),
]
