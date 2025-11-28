from django.db import models

class Asset(models.Model):
    ASSET_TYPES = [
        ('crypto', 'Crypto'),
        ('forex', 'Forex'),
        ('commodity', 'Commodity'),
        ('stock', 'Stock'),
    ]
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    type = models.CharField(max_length=10, choices=ASSET_TYPES)
    current_price = models.FloatField()
    change_percentage = models.FloatField()
    moving_average = models.FloatField()
    trend = models.CharField(max_length=5, choices=[('up', 'Up'), ('down', 'Down')])
    chart_url = models.URLField()
    hourly_income = models.FloatField()
    min_investment = models.FloatField()
    duration = models.IntegerField()
