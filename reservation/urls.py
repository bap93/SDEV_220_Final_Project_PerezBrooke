from django.urls import path
from .views import reservation_info, add_reservation_request

urlpatterns = [
    path("", reservation_info, name="reservation_info"),
    path("add_reservation_request", add_reservation_request, name="add_reservation_request"),
         
]