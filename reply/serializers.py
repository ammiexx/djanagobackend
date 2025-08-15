from rest_framework import serializers
from .models import Message, Reply

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'message', 'name', 'reply', 'created_at']

class MessageSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many=True, read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'name', 'message', 'created_at', 'replies']
