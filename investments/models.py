from django.db import models
from users.models import User
from assets.models import Asset

class UserInvestment(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('closed', 'Closed'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    invested_amount = models.FloatField()
    current_value = models.FloatField()
    units = models.FloatField()
    entry_price = models.FloatField()
    current_price = models.FloatField()
    profit_loss = models.FloatField(default=0)
    profit_loss_percentage = models.FloatField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
