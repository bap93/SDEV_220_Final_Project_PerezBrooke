from django.shortcuts import render
from reservation.forms import ReservationRequestForm
from django.http import HttpResponseRedirect, Http404
from django.db import transaction
from .models import User, ReservationBoat, ReservationRequest, Boat
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import pytz



def reservation_info(request):
    return render(request, 'reservation/reservation_info.html', {
        'reservation_request_form': ReservationRequestForm()
    })

def add_reservation_request(request):
    if request.method != 'POST':
        raise Http404("This page does not exist")
    

    form = ReservationRequestForm(request.POST)
    
    if not form.is_valid():
        return render(request, 'reservation/reservation_info.html', {
            'reservation_request_form': form
        })


    # get cleaned data
    duration = form.cleaned_data['duration']
    party_size = form.cleaned_data['party_size']
    first_name = form.cleaned_data['first_name']
    last_name = form.cleaned_data['last_name']
    age = form.cleaned_data['age']
    email = form.cleaned_data['email']
    phone_number = form.cleaned_data['phone_number']
    num_kayaks = form.cleaned_data['num_kayaks']
    num_canoes = form.cleaned_data['num_canoes']
    num_paddle_boards = form.cleaned_data['num_paddle_boards']
    date = form.cleaned_data['date']

    #duration = None
    #try: 
        # add the data to the database

    kayak = Boat.objects.get(boat_type='Kayak') 
    canoe = Boat.objects.get(boat_type='Canoe') 
    paddle_board = Boat.objects.get(boat_type='Paddle Board') 

    # Convert date string to be a timezone aware datetime object 
    #date_with_timezone = timezone.make_aware(
    #    datetime.strptime(date, '%Y-%m-%dT%H:%M'),
    #    pytz.timezone('US/Eastern')
    #)

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
                #date=date_with_timezone,
                date=date,
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

@login_required    
def admin_reservation_list(request):
    reservation_requests = ReservationRequest.objects.all()

    return render(request, 'reservation/admin_reservation_list.html', {
        'reservation_requests': reservation_requests
    })