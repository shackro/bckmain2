from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User

@csrf_exempt
def register_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = User.objects.create_user(
            username=data["email"],
            email=data["email"],
            password=data["password"],
            first_name=data["name"],
            phone_number=data["phone_number"]
        )
        return JsonResponse({"success": True, "message": "User registered", "user": {
            "id": user.id, "name": user.first_name, "email": user.email,
            "phone_number": user.phone_number, "created_at": str(user.date_joined)
        }})

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = authenticate(username=data["email"], password=data["password"])
        if user:
            login(request, user)
            return JsonResponse({"success": True, "message": "Logged in", "user": {
                "id": user.id, "name": user.first_name, "email": user.email,
                "phone_number": user.phone_number, "created_at": str(user.date_joined)
            }})
        return JsonResponse({"success": False, "message": "Invalid credentials"})

@login_required
def current_user_view(request):
    user = request.user
    return JsonResponse({"id": user.id, "name": user.first_name, "email": user.email,
                         "phone_number": user.phone_number, "created_at": str(user.date_joined)})

@login_required
def logout_view(request):
    logout(request)
    return JsonResponse({"success": True, "message": "Logged out"})
