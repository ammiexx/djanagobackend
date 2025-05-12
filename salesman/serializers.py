#salesman = employee
from rest_framework import serializers
from .models import SalesMan

class SalesManSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesMan
        fields = '__all__'




