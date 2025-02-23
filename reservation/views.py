from django.shortcuts import render
from reservation.forms import ReservationRequestForm
from django.http import HttpResponseRedirect

def reservation_info(request):
    return render(request, "reservation/reservation_info.html", {
        "reservation_request_form": ReservationRequestForm()
    })

#def add_reservation(request):
#     if request.method == "POST":
#        form = ReservationRequestForm(request.POST)
#        if form.is_valid():
#            return HttpResponseRedirect("/Thank You!/")
#
#    # if a GET (or any other method) we'll create a blank form
#    else:
#        form = ReservationRequestForm()
#
#    return render(request, ".html", {"form": form})
