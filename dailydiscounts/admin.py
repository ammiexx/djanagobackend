from django.contrib import admin
from .models import RealEstate, RealEstateImage

class ProductImageInline(admin.TabularInline):
    model = RealEstateImage
    extra = 1
    max_num = 10  # Limit to 10 images

@admin.register(RealEstate)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
