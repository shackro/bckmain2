from django.urls import path
from . import views

urlpatterns = [
    path('my/<str:phone_number>', views.my_investments),
    path('buy', views.buy_investment),
]
