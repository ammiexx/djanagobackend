from django.urls import path
from .views import ProductListCreateAPIView

urlpatterns = [
    path('RealEstates/', ProductListCreateAPIView.as_view(), name='realestate-list-create'),
]
