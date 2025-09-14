from rest_framework import serializers
from .models import RealEstate, RealEstateImage

from .models import Order, Wallet, Subscription, Refund

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = "__all__"

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"

class RefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refund
        fields = "__all__"

class RealEstateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstateImage
        fields = ['id', 'image']

class RealEstateSerializer(serializers.ModelSerializer):
    images = RealEstateImageSerializer(many=True, read_only=True)  # for reading
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )  # for writing (uploading)

    class Meta:
        model = RealEstate
        fields = '__all__'
        extra_fields = ['images', 'uploaded_images']  # include virtual fields

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        product = RealEstate.objects.create(**validated_data)

        # Save related images (limit to 10)
        for i, image in enumerate(uploaded_images):
            if i >= 10:
                break
            RealEstateImage.bjects.create(product=product, image=image)

        return RealEstate
