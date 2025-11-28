from django.db import models
from users.models import User

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0)
    equity = models.FloatField(default=0)
    currency = models.CharField(max_length=10, default="KES")
