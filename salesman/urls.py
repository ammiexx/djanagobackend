from django.urls import path
from .views import SalesManListCreateView

urlpatterns = [
    path('saleman/',SalesManListCreateView.as_view(), name='salesman'),
]
