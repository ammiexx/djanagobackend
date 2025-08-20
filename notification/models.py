from django.db import models
from customer.models import Customer
from salesman.models import SalesMan
from postproduct.models import PostProduct
class Notification(models.Model):
    SenderId = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='notifications',max_length=50)
    RecieverId=models.ForeignKey(SalesMan,on_delete=models.CASCADE,related_name='notifications',max_length=50)
    ItemId=models.ForeignKey(PostProduct,on_delete=models.CASCADE,related_name='notification',max_length=50)
    comment = models.TextField(max_length=250,null=True,blank=True)
    SenderName=models.TextField(max_length=100,null=True,blank=True)
    date= models.DateTimeField(auto_now=True)
    is_read=models.BooleanField(default=False)
    notification_type=models.CharField(max_length=50,choices=[
      
       ('message','Message'),
       ('alert','Alert'),
       ('remainder','Remainder'),
       ('update','Update'),

    ],default='message')
    priority=models.CharField(max_length=50,choices=[
        ('low','Low'),
        ('medium','Medium'),
        ('hight','High'),
    ],default='medium')
    
    def __str__(self):
        return f"notification for {self.SenderName}"
   

   
