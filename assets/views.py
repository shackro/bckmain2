from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Asset

@login_required
def market_assets(request):
    assets = Asset.objects.all()
    data = [{
        "id": asset.id,
        "name": asset.name,
        "symbol": asset.symbol,
        "type": asset.type,
        "current_price": asset.current_price,
        "change_percentage": asset.change_percentage,
        "moving_average": asset.moving_average,
        "trend": asset.trend,
        "chart_url": asset.chart_url,
        "hourly_income": asset.hourly_income,
        "min_investment": asset.min_investment,
        "duration": asset.duration,
    } for asset in assets]
    return JsonResponse(data, safe=False)
