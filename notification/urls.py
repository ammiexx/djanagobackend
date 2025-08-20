from django.urls import path
from .views import NotificationListCreateView

from django.urls import path
from .views import (
    NotificationListCreateView,
    NotificationSearchView,
    NotificationRetrieveUpdateView,
    NotificationDestroyView,
)
urlpatterns = [
    path('notifications/', NotificationListCreateView.as_view(), name='customer-list-create'),
    path('notifications/search/', NotificationSearchView.as_view(), name='customer-search'),
    path('notifications/<int:pk>/update/', NotificationRetrieveUpdateView.as_view(), name='customer-update'),
    path('notifications/<int:pk>/delete/', NotificationDestroyView.as_view(), name='customer-delete'),
]
