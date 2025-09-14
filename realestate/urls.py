from django.urls import path
from .views import ProductListCreateAPIView
from .views import create_checkout_session

from .views import (
    PaymentUpdatesAPIView,
    PendingOrdersAPIView,
    CompletedOrdersAPIView,
    WalletAPIView,
    SubscriptionsAPIView,
    RefundsAPIView,
)

urlpatterns = [
    path('RealEstates/', ProductListCreateAPIView.as_view(), name='realestate-list-create'),
    path("create-checkout-session/", create_checkout_session, name="create-checkout-session"),
    path("payment-updates/", PaymentUpdatesAPIView.as_view(), name="payment-updates"),
    path("orders/pending/", PendingOrdersAPIView.as_view(), name="pending-orders"),
    path("orders/completed/", CompletedOrdersAPIView.as_view(), name="completed-orders"),
    path("wallet/", WalletAPIView.as_view(), name="wallet"),
    path("subscriptions/", SubscriptionsAPIView.as_view(), name="subscriptions"),
    path("refunds/", RefundsAPIView.as_view(), name="refunds"),
    
]
