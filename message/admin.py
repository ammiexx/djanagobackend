# admin.py
from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'created_at')
    search_fields = ('name', 'message')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
