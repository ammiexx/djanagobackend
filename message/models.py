# models.py
from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=100, blank=True)  # optional name
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name or 'Anonymous'}: {self.message[:20]}"
