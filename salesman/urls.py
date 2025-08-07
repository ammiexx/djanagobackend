from django.urls import path
from .views import (
    SalesManListCreateView,
    SalesManSearchView,
    SalesManRetrieveUpdateView,
    SalesManDestroyView
)
urlpatterns = [
    path('salesmans/', SalesManListCreateView.as_view(), name='customer-list-create'),
    path('salesmans/search/', SalesManSearchView.as_view(), name='customer-search'),
    path('salesmans/<int:pk>/update/', SalesManRetrieveUpdateView.as_view(), name='customer-update'),
    path('salesmans/<int:pk>/delete/', SalesManDestroyView.as_view(), name='customer-delete'),
]
