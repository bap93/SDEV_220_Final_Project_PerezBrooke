from django import forms
from datetime import datetime


class ReservationRequestForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields = {
            'first_name': forms.CharField(
                initial = 'Brando',
                widget = forms.TextInput( attrs = {
                    'class': 'form-control'
                })
            ),
            'last_name': forms.CharField(
                initial = 'Slorm',
                widget = forms.TextInput( attrs = {
                    'class': 'form-control'
                })
            ),
            'age': forms.IntegerField(
                initial = 16,
                widget = forms.NumberInput( attrs = {
                    'class': 'form-control'
                })
            ),
            'email': forms.CharField(
                initial = 'foo@example.net',
                widget = forms.TextInput( attrs = {
                    'class': 'form-control'
                })
            ),
            'phone_number': forms.CharField(
                initial = '555-555-5555',
                widget = forms.TextInput( attrs = {
                    'class': 'form-control'
                })
            ),
            'date': forms.DateTimeField(
                initial = datetime.now().strftime('%Y-%m-%dT%H:%M'),
                widget  = forms.DateTimeInput( attrs = {
                    'class': 'form-control',
                    'type': 'datetime-local'
                }
            )),
            'party_size': forms.IntegerField(
                initial = 2,
                widget = forms.NumberInput( attrs = {
                    'class': 'form-control',
                    'min': 1
                })
            ),
            'num_kayaks': forms.IntegerField(
                initial = 1,
                label = "Number of Kayaks",
                widget = forms.NumberInput( attrs = {
                    'class': 'form-control',
                    'min': 1
                })
            ),
            'num_canoes': forms.IntegerField(
                initial = 2,
                label = "Number of Canoes",
                widget = forms.NumberInput( attrs = {
                    'class': 'form-control',
                    'min': 1
                })
            ),
            'num_paddle_boards': forms.IntegerField(
                initial = 3,
                label = "Number of Paddle Boards",
                widget = forms.NumberInput( attrs = {
                    'class': 'form-control',
                    'min': 1
                })
            ),
            'duration': forms.DurationField(
                initial = 2,
                widget = forms.NumberInput( attrs = {
                    'class': 'form-control',
                    'min': 1,
                    'max': 2
                }
            ))
        }
        