from django.urls import path, include
from .views import reservation_info, add_reservation_request, delete_reservation, admin_reservation_list, reservation_logout

urlpatterns = [
    path('', reservation_info, name='reservation_info'),
    path('add_reservation_request', add_reservation_request, name='add_reservation_request'),
    path('admin_reservation_list', admin_reservation_list, name = 'admin_reservation_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('delete_reservation', delete_reservation, name = 'delete_reservation'),    
    path('logout/', reservation_logout, name='reservation_logout'),
]
