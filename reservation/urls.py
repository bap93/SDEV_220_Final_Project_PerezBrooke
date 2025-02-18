from django.urls import path
from .views import reservation_info, reservation_request

urlpatterns = [
    path("", reservation_info, name="reservation_info"),
    path("request/", reservation_request, name="reservation_request"),
         
]