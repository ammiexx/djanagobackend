from rest_framework import serializers
from .models import Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ['id', 'image']

    def get_image(self, obj):
        return obj.image.url if obj.image else None


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )

    product_photo = serializers.SerializerMethodField()
    profile_photo = serializers.SerializerMethodField()

    def get_product_photo(self, obj):
        return obj.product_photo.url if obj.product_photo else None

    def get_profile_photo(self, obj):
        return obj.profile_photo.url if obj.profile_photo else None

    class Meta:
        model = Product
        fields = '__all__'  # all fields from model
        extra_fields = ['images', 'uploaded_images', 'product_photo', 'profile_photo']

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        product = Product.objects.create(**validated_data)

        # Save related images (limit to 10)
        for i, image in enumerate(uploaded_images):
            if i >= 10:
                break
            ProductImage.objects.create(product=product, image=image)

        return product
