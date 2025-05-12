from django.db import models
from customer.models import Customer
from salesman.models import SalesMan
from postproduct.models import PostProduct
class Notification(models.Model):
    SenderId = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='notifications',max_length=50)
    RecieverId=models.ForeignKey(SalesMan,on_delete=models.CASCADE,related_name='notifications',max_length=50)
    wrokId=models.ForeignKey(PostProduct,on_delete=models.CASCADE,related_name='notification',max_length=50)
    comment = models.TextField()
    SenderName=models.TextField(max_length=100)
    Date= models.DateTimeField(auto_now_add=True)
    rate = models.PositiveSmallIntegerField()
    def __str__(self):
        return f"Notification for {self.employer_kyc.company_name}"

   

   
