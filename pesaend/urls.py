from datetime import timezone
from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/wallet/', include('wallet.urls')),
    path('api/investments/', include('investments.urls')),
    path('api/assets/', include('assets.urls')),
    path('api/activities/', include('activities.urls')),
    path('api/health', lambda request: JsonResponse({"status": "ok", "service": "pesaend", "timestamp": str(timezone.now())}))
]
