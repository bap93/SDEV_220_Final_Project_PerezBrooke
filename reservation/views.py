from django.shortcuts import render
from reservation.forms import ReservationRequestForm
from django.http import HttpResponseRedirect, Http404
from django.db import transaction
from .models import User, ReservationBoat, ReservationRequest, Boat
from datetime import datetime
from django.utils import timezone
import pytz



def reservation_info(request):
    return render(request, "reservation/reservation_info.html", {
        "reservation_request_form": ReservationRequestForm()
    })

def add_reservation_request(request):
    if request.method != "POST":
        raise Http404("This page does not exist")
    


    form = ReservationRequestForm(request.POST)
    duration = None
    try: 
        # add the data to the database
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        num_kayaks = int(request.POST.get('num_kayaks'))
        num_canoes = int(request.POST.get('num_canoes'))
        num_paddle_boards = int(request.POST.get('num_paddle_boards'))
        date = request.POST.get('date')

        # retrieve and validate party size
        party_size = int(request.POST.get('party_size'))
        if( party_size < 1 or party_size > 50 ):
            raise ValueError("Party Size must be between 1 and 50.")

        # retriev and validate duration
        duration = int(request.POST.get("duration"))
        if(duration <1 or duration >2):
            raise ValueError("Duration must be entered in the form of 1 or 2.")
        
    except (ValueError, TypeError) as e:
        return render(request, "reservation/reservation_info.html",{
            "reservation_request_form": form,
            "error": e
        })

    kayak = Boat.objects.get(boat_type='Kayak') 
    canoe = Boat.objects.get(boat_type='Canoe') 
    paddle_board = Boat.objects.get(boat_type='Paddle Board') 

    # Convert date string to be a timezone aware datetime object 
    date_with_timezone = timezone.make_aware(
        datetime.strptime(date, '%Y-%m-%dT%H:%M'),
        pytz.timezone('US/Eastern')
    )

    try:
        with transaction.atomic():
            # Step 1: Add information to the User table
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                age=age
            )

            # Step 2: Add information to the ReservationRequest table
            reservation = ReservationRequest.objects.create(
                user=user,
                date=date_with_timezone,
                #date=date,
                party_size=party_size,
                duration=duration
            )

            # Step 3: Add multiple records in ReservationBoat
            for num in range(num_kayaks):
                ReservationBoat.objects.create(
                    reservation=reservation,
                    boat_type=kayak
                )
            
            for num in range(num_canoes):
                ReservationBoat.objects.create(
                    reservation=reservation,
                    boat_type=canoe
                )
            
            for num in range(num_paddle_boards):
                ReservationBoat.objects.create(
                    reservation=reservation,
                    boat_type=paddle_board
                )

            # If everything succeeds, the transaction will be committed
            return render(request, 'reservation/add_reservation_request_success.html',{
                'reservation_data': {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'phone_number': phone_number,
                    'num_kayaks': num_kayaks,
                    'num_canoes': num_canoes,
                    'num_paddles_boards': num_paddle_boards,
                    'date': date,
                    'party_size': party_size,
                    'duration': duration
                }
            })

    except Exception as e:
        # If any error occurs, the transaction will be rolled back
        raise Exception(f"Error occurred adding reservation: {e}")