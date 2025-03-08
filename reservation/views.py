from django.shortcuts import render, redirect
from reservation.forms import ReservationRequestForm
from django.http import Http404
from django.db import transaction
from .models import User, ReservationBoat, ReservationRequest, Boat
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

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
    
    # let customer know if they choose a time past reservation hours and have them retry
    date = form.cleaned_data['date']
    if date.hour <8 or date.hour >=18: 
        form.add_error('date', "Please make your request for between 8am and 6pm")
        return render(request, 'reservation/reservation_info.html', {'reservation_request_form':form})

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

    kayak = Boat.objects.get(boat_type='Kayak') 
    canoe = Boat.objects.get(boat_type='Canoe') 
    paddle_board = Boat.objects.get(boat_type='Paddle Board') 

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

# require login for admin reservation list page
@login_required    
def admin_reservation_list(request):
    reservation_requests = ReservationRequest.objects.all()

    return render(request, 'reservation/admin_reservation_list.html', {
        'reservation_requests': reservation_requests
    })

# deletes from database and admin reservation list page
def delete_reservation(request):
    if request.method != 'POST':
        raise Http404("This page does not exist")
    
    try:
        user_id = int(request.POST.get('user_id'))
        user = User.objects.get(id = user_id)
        user.delete()

    except Exception as e:
        raise Http404(f"Error removing user with id '{user_id}': {e}")
    
    reservation_requests = ReservationRequest.objects.all()
    return render(request, 'reservation/admin_reservation_list.html', {
        'reservation_requests': reservation_requests
    })

# logs out of admin reservation list page
def reservation_logout(request):
    logout(request)
    return render(request, 'reservation/reservation_info.html', {
        'reservation_request_form': ReservationRequestForm()
    })
