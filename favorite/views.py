from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Favorite
from .serializers import FavoriteSerializer

class FavoriteListCreateView(generics.ListCreateAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ToggleFavoriteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        target_id = request.data.get('target_id')
        target_type = request.data.get('target_type')

        if not target_id or not target_type:
            return Response({'error': 'target_id and target_type are required'}, status=status.HTTP_400_BAD_REQUEST)

        favorite, created = Favorite.objects.get_or_create(
            user=request.user,
            target_id=target_id,
            target_type=target_type
        )

        if not created:
            favorite.delete()
            return Response({'status': 'removed'})
        return Response({'status': 'added'})
