from django.db import models
from django.contrib.auth.models import User

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target_id = models.IntegerField()
    target_type = models.CharField(max_length=10, choices=[('buyer', 'Buyer'), ('seller', 'Seller')])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'target_id', 'target_type')
