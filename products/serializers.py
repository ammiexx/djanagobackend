from rest_framework import serializers
from .models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ['id', 'image']

    def get_image(self, obj):
        try:
            return obj.image.url if obj.image else None
        except Exception:
            return None


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    # Handle Cloudinary fields properly
    product_photo = serializers.SerializerMethodField()
    profile_photo = serializers.SerializerMethodField()

    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )

    class Meta:
        model = Product
        fields = '__all__'

    def get_product_photo(self, obj):
        try:
            return obj.product_photo.url if obj.product_photo else None
        except Exception:
            return None

    def get_profile_photo(self, obj):
        try:
            return obj.profile_photo.url if obj.profile_photo else None
        except Exception:
            return None

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        product = Product.objects.create(**validated_data)

        for i, image in enumerate(uploaded_images):
            if i >= 10:
                break
            ProductImage.objects.create(product=product, image=image)

        return product
