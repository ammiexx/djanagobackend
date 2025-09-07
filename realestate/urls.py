from django.urls import path
from .views import ProductListCreateAPIView
<<<<<<< HEAD
from .views import create_checkout_session

urlpatterns = [
    path('RealEstates/', ProductListCreateAPIView.as_view(), name='realestate-list-create'),
    path("api/create-checkout-session/", create_checkout_session, name="create-checkout-session"),
    
=======

urlpatterns = [
    path('RealEstates/', ProductListCreateAPIView.as_view(), name='realestate-list-create'),
>>>>>>> 3cf6f522ea88383a9117ee65a09e02a75541438a
]
