from django.urls import path
from . import views

urlpatterns = [
    path('balance/<str:phone_number>', views.wallet_balance),
    path('deposit', views.deposit),
    path('withdraw', views.withdraw),
]
