from django.db import models

class Product(models.Model):
    first_name = models.CharField(max_length=100,null=True, blank=True)
    last_name = models.CharField(max_length=100,null=True, blank=True)
    profile_photo = models.ImageField(upload_to='images/',null=True, blank=True)
    product_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_photo = models.ImageField(upload_to='pimages/',null=True, blank=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100,default="general")
    condition = models.CharField(max_length=50, choices=[('new', 'New'), ('used', 'Used')],null=True, blank=True)
    location = models.CharField(max_length=255,null=True, blank=True)
    contact_telegram = models.URLField(blank=True,null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.product_name
