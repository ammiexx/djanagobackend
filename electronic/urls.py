from django.urls import path
from .views import ProductListCreateAPIView

urlpatterns = [
    path('electronic/', ProductListCreateAPIView.as_view(), name='realestate-list-create'),
]
