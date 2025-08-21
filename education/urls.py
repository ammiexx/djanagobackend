from django.urls import path
from .views import ProductListCreateAPIView

urlpatterns = [
    path('educations/', ProductListCreateAPIView.as_view(), name='product-list-create'),
]
