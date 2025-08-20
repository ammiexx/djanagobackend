# chat/urls.py

from django.urls import path
from .views import (
    BuyerListCreateView, BuyerDetailView,
    SellerListCreateView, SellerDetailView,
    ChatListCreateView, ChatDetailView,
)

urlpatterns = [
    path('buyers/', BuyerListCreateView.as_view(), name='buyer-list'),
    path('buyers/<int:pk>/', BuyerDetailView.as_view(), name='buyer-detail'),
    
    path('sellers/', SellerListCreateView.as_view(), name='seller-list'),
    path('sellers/<int:pk>/', SellerDetailView.as_view(), name='seller-detail'),
    
    path('chats/', ChatListCreateView.as_view(), name='chat-list'),
    path('chats/<int:pk>/', ChatDetailView.as_view(), name='chat-detail'),
]
