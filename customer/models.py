from django.db import models
class Customer(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    detail = models.TextField()
    profession = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=255)  
    cimage = models.CharField(max_length=255) 
    datas = models.TextField(blank=True)  
    data = models.TextField(blank=True)     
    date = models.DateTimeField()  
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=20)
   
    def __str__(self):
        return f"{self.fname} {self.lname} - {self.profession}"


