from django.urls import path

from django.urls import path
from .views import (
    ProductListCreateView,
    ProductSearchView,
    ProductRetrieveUpdateView,
    ProdcutDestroyView,
)
urlpatterns = [
    path('postproduct/', ProductListCreateView.as_view(), name='customer-list-create'),
    path('postproduct/search/', ProductSearchView.as_view(), name='customer-search'),
    path('postproduct/<int:pk>/update/', ProductRetrieveUpdateView.as_view(), name='customer-update'),
    path('postproduct/<int:pk>/delete/', ProdcutDestroyView.as_view(), name='customer-delete'),
]
