from django.shortcuts import render
from reservation.forms import ReservationRequestForm

def reservation_info(request):
    return render(request, "reservation/reservation_info.html")

def reservation_request(request):
    if request.method == "POST":
        form = ReservationRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "reservation/request_success.html")
    else:
        form = ReservationRequestForm()
    return render(request, "reservation/reservation_request.html", {"form": form})
