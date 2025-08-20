from django.db import models
from customer.models import Customer
class PostProduct(models.Model):
    customerId= models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='jobs')
    postername = models.CharField(max_length=255,blank=True,null=True)
    payment = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    ion = models.TextField(max_length=255,null=True,blank=True)
    pro = models.CharField(max_length=100,null=True,blank=True)
    title = models.CharField(max_length=255,blank=True,null=True)
    image = models.ImageField(blank=True, default='',null=True)
    type = models.CharField(max_length=10, default='3',null=True)
    date = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return f"{self.title} - {self.postername}"
