# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('cat', views.cat_messages, name='cat_messages'),
]
