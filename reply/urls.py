from django.urls import path
from .views import MessageListCreate, ReplyListCreate

urlpatterns = [
    path('api/cat', MessageListCreate.as_view()),       # existing message API
    path('api/reply', ReplyListCreate.as_view()),       # reply API
]
