from rest_framework import serializers
from .models import Favorite

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'user', 'target_id', 'target_type', 'created_at']
        read_only_fields = ['user', 'created_at']
