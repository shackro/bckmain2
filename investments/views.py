from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import UserInvestment
from assets.models import Asset
from users.models import User
import json

@login_required
def my_investments(request, phone_number):
    investments = UserInvestment.objects.filter(user__phone_number=phone_number)
    data = [{
        "id": inv.id,
        "user_phone": inv.user.phone_number,
        "asset_id": inv.asset.id,
        "asset_name": inv.asset.name,
        "invested_amount": inv.invested_amount,
        "current_value": inv.current_value,
        "units": inv.units,
        "entry_price": inv.entry_price,
        "current_price": inv.current_price,
        "profit_loss": inv.profit_loss,
        "profit_loss_percentage": inv.profit_loss_percentage,
        "status": inv.status,
        "created_at": str(inv.created_at),
    } for inv in investments]
    return JsonResponse(data, safe=False)

@csrf_exempt
@login_required
def buy_investment(request):
    data = json.loads(request.body)
    user = User.objects.get(phone_number=data["phone_number"])
    asset = Asset.objects.get(id=data["asset_id"])
    units = data["amount"] / asset.current_price

    investment = UserInvestment.objects.create(
        user=user,
        asset=asset,
        invested_amount=data["amount"],
        current_value=data["amount"],
        units=units,
        entry_price=asset.current_price,
        current_price=asset.current_price,
    )
    return JsonResponse({"success": True, "message": "Investment bought", "investment_id": investment.id})
