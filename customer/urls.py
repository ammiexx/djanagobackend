from django.urls import path
from .views import CustomerCListCreateView

urlpatterns = [
     path('customers/', CustomerCListCreateView.as_view(), name='customer-list-create'),# for post
]
