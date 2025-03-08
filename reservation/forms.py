from django import forms
from phonenumber_field.formfields import PhoneNumberField

class ReservationRequestForm(forms.Form):

    first_name = forms.CharField(
        max_length = 50,
        widget = forms.TextInput( attrs = {
            'class': 'form-control',
        })
    )

    last_name = forms.CharField(
        max_length = 50,
        widget = forms.TextInput( attrs = {
            'class': 'form-control'
        })
    )

    age = forms.IntegerField( 
        max_value= 120,
        min_value= 16,
        widget = forms.NumberInput( attrs = {
            'class': 'form-control',
        })
    )

    email = forms.EmailField(
        max_length = 250,
        widget = forms.TextInput( attrs = {
            'class': 'form-control'
        })
    )

    phone_number = PhoneNumberField(
        widget = forms.TextInput( attrs = {
            'class': 'form-control'
        })
    )

    date = forms.DateTimeField(
        widget  = forms.DateTimeInput( attrs = {
            'class': 'form-control',
            'type': 'datetime-local'
        })
    )

    duration = forms.IntegerField(
        min_value = 1,
        max_value = 2,
        widget = forms.NumberInput( attrs = {
            'class': 'form-control'
        })
    )

    party_size = forms.IntegerField(
        min_value= 1,
        max_value = 50,
        widget = forms.NumberInput( attrs = {
            'class': 'form-control',
        })
    )

    num_kayaks = forms.IntegerField(
        min_value= 0,
        max_value= 50,
        label = "Number of Kayaks",
        widget = forms.NumberInput( attrs = {
            'class': 'form-control',
        })
    )
        
    num_canoes = forms.IntegerField(
        min_value = 0,
        max_value = 50,
        label = "Number of Canoes",
        widget = forms.NumberInput( attrs = {
            'class': 'form-control',
        })
    )

    num_paddle_boards = forms.IntegerField(
        min_value = 0, 
        max_value = 50,
        label = "Number of Paddle Boards",
        widget = forms.NumberInput( attrs = {
            'class': 'form-control',
        })
    )
    

            
          
          
       
        