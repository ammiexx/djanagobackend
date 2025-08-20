from django.urls import path
from .views import FavoriteListCreateView, ToggleFavoriteView

urlpatterns = [
    path('favorites/', FavoriteListCreateView.as_view(), name='favorites'),
    path('favorites/toggle/', ToggleFavoriteView.as_view(), name='toggle-favorite'),
]
