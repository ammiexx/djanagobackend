

from django.db import models
class SalesMan(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    detail = models.TextField()
    profession = models.CharField(max_length=100)
    password = models.CharField(max_length=128)  # Store hashed passwords ideally
    name = models.CharField(max_length=255)      # Possibly image name
    cimage = models.CharField(max_length=255)    # Possibly second image name
    datas = models.TextField(blank=True)         # Image data (base64 or string)
    data = models.TextField(blank=True)          # Another image data field
    date = models.DateTimeField()                # From the Flutter 'd' variable
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=20)
   
    def __str__(self):
        return f"{self.fname} {self.lname} - {self.profession}"




