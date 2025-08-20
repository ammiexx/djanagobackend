# chat/models.py

from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    profile_photo = models.URLField()
    telegram = models.URLField(blank=True, null=True)
    tiktok = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    profile_photo = models.URLField()
    telegram = models.URLField(blank=True, null=True)
    tiktok = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Chat(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='chats')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='chats')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat between {self.buyer.name} and {self.seller.name}"
