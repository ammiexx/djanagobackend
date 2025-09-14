from django.db import models

class RealEstate(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    profile_photo = models.ImageField(upload_to='images/', null=True, blank=True)
    product_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    product_photo = models.ImageField(upload_to='pimages/', null=True, blank=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, default="reale estate")
    condition = models.CharField(
        max_length=50,
        choices=[('new', 'New'), ('used', 'Used')],
        null=True,
        blank=True
    )
    location = models.CharField(max_length=255, null=True, blank=True)
    contact_telegram = models.URLField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.product_name

class RealEstateImage(models.Model):
    product = models.ForeignKey(RealEstate, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pimages/')

    def __str__(self):
        return f"Image for {self.product.product_name}"
from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("refunded", "Refunded"),
    ]

    stripe_session_id = models.CharField(max_length=255)
    customer_email = models.EmailField(null=True, blank=True)
    product_id = models.IntegerField(null=True, blank=True)  # store React product id
    product_name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    specs = models.JSONField(null=True, blank=True)  # list of specs
    quantity = models.IntegerField(default=1)
    amount_total = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    status = models.CharField(max_length=50, default="pending")

    def __str__(self):
        return f"{self.product_name} - {self.status}"


class Wallet(models.Model):
    user_email = models.EmailField()
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user_email} - {self.balance} ETB"


class Subscription(models.Model):
    user_email = models.EmailField()
    plan_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user_email} - {self.plan_name}"


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="refunds")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Refund {self.amount} for Order {self.order.id}"
