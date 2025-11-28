from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import UserActivity
from django.views.decorators.csrf import csrf_exempt
import json
from users.models import User

@login_required
def my_activities(request, phone_number):
    activities = UserActivity.objects.filter(user__phone_number=phone_number)
    data = [{
        "id": act.id,
        "user_phone": act.user.phone_number,
        "activity_type": act.activity_type,
        "amount": act.amount,
        "description": act.description,
        "timestamp": str(act.timestamp),
        "status": act.status
    } for act in activities]
    return JsonResponse(data, safe=False)
