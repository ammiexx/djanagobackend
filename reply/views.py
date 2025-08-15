from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Message, Reply
from .serializers import MessageSerializer, ReplySerializer

class MessageListCreate(APIView):
    def get(self, request):
        messages = Message.objects.all().order_by('-created_at')
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReplyListCreate(APIView):
    def get(self, request):
        message_id = request.query_params.get('messageId')
        if message_id:
            replies = Reply.objects.filter(message_id=message_id).order_by('created_at')
        else:
            replies = Reply.objects.all().order_by('created_at')
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
