from rest_framework import serializers
from .models import Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)  # for reading
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )  # for writing (uploading)

    class Meta:
        model = Product
        fields = '__all__'
        extra_fields = ['images', 'uploaded_images']  # include virtual fields

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        product = Product.objects.create(**validated_data)

        # Save related images (limit to 10)
        for i, image in enumerate(uploaded_images):
            if i >= 10:
                break
            ProductImage.objects.create(product=product, image=image)

        return product
