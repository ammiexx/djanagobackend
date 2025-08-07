from rest_framework import serializers
from .models import PostProduct
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostProduct
        fields = '__all__'