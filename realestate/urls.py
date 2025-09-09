from django.urls import path
from .views import ProductListCreateAPIView
from .views import create_checkout_session

urlpatterns = [
    path('RealEstates/', ProductListCreateAPIView.as_view(), name='realestate-list-create'),
    path("create-checkout-session/", create_checkout_session, name="create-checkout-session"),
    
]
