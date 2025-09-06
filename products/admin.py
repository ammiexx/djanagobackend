from django.contrib import admin
from .models import Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    max_num = 10  # Limit to 10 images

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ("product_name", "company_name", "category", "verified", "date_posted")
    list_filter = ("verified", "category")
    search_fields = ("product_name", "company_name")
    actions = ["mark_verified", "mark_unverified"]

    def mark_verified(self, request, queryset):
        queryset.update(verified=True)
    mark_verified.short_description = "Mark selected products as Verified"

    def mark_unverified(self, request, queryset):
        queryset.update(verified=False)
    mark_unverified.short_description = "Mark selected products as Unverified"
