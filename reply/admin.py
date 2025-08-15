from django.contrib import admin
from .models import Message, Reply

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'message', 'created_at')
    search_fields = ('name', 'message')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'name', 'reply', 'created_at')
    search_fields = ('name', 'reply')
    list_filter = ('created_at',)
    ordering = ('created_at',)
