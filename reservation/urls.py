from django.urls import path
from .views import reservation_info

urlpatterns = [
    path("", reservation_info, name="reservation_info"),
         
]