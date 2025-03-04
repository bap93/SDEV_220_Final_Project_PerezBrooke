from django import forms
from datetime import datetime
from phonenumber_field.formfields import PhoneNumberField
from django.core.validators import EmailValidator


class ReservationRequestForm(forms.Form):

    first_name = forms.CharField(
        initial = 'Brando',
        max_length = 50,
        widget = forms.TextInput( attrs = {
            'class': 'form-control',
        })
    )

    last_name = forms.CharField(
        initial = 'Slorm',
        max_length = 50,
        widget = forms.TextInput( attrs = {
            'class': 'form-control'
        })
    )

    age = forms.IntegerField( 
        max_value= 120,
        min_value= 16,
        initial = 16,
        widget = forms.NumberInput( attrs = {
            'class': 'form-control',

        })
    )

    email = forms.EmailField(
        initial = 'foo@example.net',
        max_length = 250,
        widget = forms.TextInput( attrs = {
            'class': 'form-control'
        })
    )

    phone_number = PhoneNumberField(
        initial = '555-555-5555',
        widget = forms.TextInput( attrs = {
            'class': 'form-control'
        })
    )

    date = forms.DateTimeField(
        initial = datetime.now().strftime('%Y-%m-%dT%H:%M'),
        widget  = forms.DateTimeInput( attrs = {
            'class': 'form-control',
            'type': 'datetime-local'
        })
    )

    duration = forms.IntegerField(
        initial = 2,
        min_value = 1,
        max_value = 2,
        widget = forms.NumberInput( attrs = {
            'class': 'form-control'
        })
    )

    party_size = forms.IntegerField(
        initial = 2,
        min_value= 1,
        max_value = 50,
        widget = forms.NumberInput( attrs = {
            'class': 'form-control',
        })
    )

    
    num_kayaks = forms.IntegerField(
        initial = 1,
        min_value= 0,
        max_value= 50,
        label = "Number of Kayaks",
        widget = forms.NumberInput( attrs = {
            'class': 'form-control',
        })
    )
        
    num_canoes = forms.IntegerField(
        initial = 2,
        min_value = 0,
        max_value = 50,
        label = "Number of Canoes",
        widget = forms.NumberInput( attrs = {
            'class': 'form-control',
  
        })
    )

    num_paddle_boards = forms.IntegerField(
        initial = 3,
        min_value = 0, 
        max_value = 50,
        label = "Number of Paddle Boards",
        widget = forms.NumberInput( attrs = {
            'class': 'form-control',

        })
    )
    

            
          
          
       
        