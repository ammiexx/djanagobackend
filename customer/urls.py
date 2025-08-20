from django.urls import path
from .views import (
    CustomerCListCreateView,
    CustomerSearchView,
    CustomerRetrieveUpdateView,
    CustomerDestroyView,
)
urlpatterns = [
    path('customers/', CustomerCListCreateView.as_view(), name='customer-list-create'),
    path('customers/search/', CustomerSearchView.as_view(), name='customer-search'),
    path('customers/<int:pk>/update/', CustomerRetrieveUpdateView.as_view(), name='customer-update'),
    path('customers/<int:pk>/delete/', CustomerDestroyView.as_view(), name='customer-delete'),
]


#http://127.0.0.1:8000/api/customers/
#http://127.0.0.1:8000/api/customers/
#http://127.0.0.1:8000/api/customers/search/?search=animut
#http://127.0.0.1:8000/api/customers/3/update/
#http://127.0.0.1:8000/api/customers/3/delete/