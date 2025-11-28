from django.urls import path
from . import views

urlpatterns = [
    path('my/<str:phone_number>', views.my_activities),
]
