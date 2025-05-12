from django.db import models
from customer.models import Customer
class PostProduct(models.Model):
    customerId= models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='jobs')
    empname = models.CharField(max_length=255)
    payment = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    description = models.TextField()
    pro = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    image = models.TextField(blank=True, default='')
    type = models.CharField(max_length=10, default='2')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.empname}"
