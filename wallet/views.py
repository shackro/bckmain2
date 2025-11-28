from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Wallet
from django.views.decorators.csrf import csrf_exempt
import json

@login_required
def wallet_balance(request, phone_number):
    wallet = Wallet.objects.get(user__phone_number=phone_number)
    return JsonResponse({"balance": wallet.balance, "equity": wallet.equity, "currency": wallet.currency})

@csrf_exempt
@login_required
def deposit(request):
    data = json.loads(request.body)
    wallet = Wallet.objects.get(user__phone_number=data["phone_number"])
    wallet.balance += data["amount"]
    wallet.save()
    return JsonResponse({"success": True, "message": "Deposited", "new_balance": wallet.balance, "new_equity": wallet.equity})

@csrf_exempt
@login_required
def withdraw(request):
    data = json.loads(request.body)
    wallet = Wallet.objects.get(user__phone_number=data["phone_number"])
    if wallet.balance >= data["amount"]:
        wallet.balance -= data["amount"]
        wallet.save()
        return JsonResponse({"success": True, "message": "Withdrawn", "new_balance": wallet.balance, "new_equity": wallet.equity})
    return JsonResponse({"success": False, "message": "Insufficient funds"})
