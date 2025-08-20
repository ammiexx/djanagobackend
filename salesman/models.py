

from django.db import models

class SalesMan(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255, blank=True)
    detail = models.TextField(blank=True)
    profession = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=255, blank=True)
    pimage=models.ImageField(upload_to='images/',null=True,blank=True)
    cimage = models.ImageField(upload_to='images/',null=True,blank=True) 
    datas = models.TextField(blank=True) 
    data = models.TextField(blank=True) 
    date = models.DateTimeField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True) 
    phone = models.CharField(max_length=20, blank=True)
    type = models.IntegerField(default=2, null=True, blank=True)

    def __str__(self):
        return f"{self.fname} {self.lname} - {self.profession}"





