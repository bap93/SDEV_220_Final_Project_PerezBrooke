from django.shortcuts import render
from reservation.forms import ReservationRequestForm
from django.http import HttpResponseRedirect, Http404


def reservation_info(request):
    return render(request, "reservation/reservation_info.html", {
        "reservation_request_form": ReservationRequestForm()
    })

def add_reservation_request(request):
    if request.method != "POST":
        raise Http404("This page does not exist")
    
    else:
        reservation_data = {
            "duration": request.POST.get("duration"),
            "date": request.POST.get("date"),
            "party_size": request.POST.get("party_size"),
        }
        return render(request, "reservation/add_reservation_request_success.html", 
                      {
                          "reservation_data": reservation_data
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
