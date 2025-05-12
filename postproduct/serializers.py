from rest_framework import serializers
from .models import PostProduct
class JobSerializer(serializers.ModelSerializer):
    class meta:
        model = PostProduct
        fields = '__all__'