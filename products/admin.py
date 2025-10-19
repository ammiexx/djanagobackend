from django.contrib import admin
from .models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    max_num = 10  # Limit to 10 images


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ("product_name", "company_name", "category", "verified", "date_posted","location","contact_phone",
                    "contact_telegram","contact_tick","web_site",)
    list_filter = ("verified", "category")
    search_fields = ("product_name", "company_name", "email")
    actions = ["mark_verified", "mark_unverified"]
    list_editable = ("verified",)
    fields = (
        "product_name", "company_name", "category", "verified",
        "latitude", "longitude","discount_start_date","discount_duration","profile_photo",
        "location", "contact_phone", "contact_telegram", "contact_tick",
        "web_site", "discount", "condition", "description",
        "product_photo", "product_video"
    )
    class Media:
        js = ("products/admin_geolocation.js",)
    def mark_verified(self, request, queryset):
        updated = queryset.update(verified=True)
        self.message_user(request, f"{updated} product(s) marked as Verified ✅")
    mark_verified.short_description = "Mark selected products as Verified"

    def mark_unverified(self, request, queryset):
        updated = queryset.update(verified=False)
        self.message_user(request, f"{updated} product(s) marked as Unverified ❌")
    mark_unverified.short_description = "Mark selected products as Unverified"
