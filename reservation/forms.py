from django import forms
from .models import ReservationRequest


class ReservationRequestForm(forms.ModelForm):
    class Meta:
        model = ReservationRequest
        fields =[
            "date",
            "party_size",
            "duration",
        ]
        widgets = {
            "date": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "class": "form-control",                   
                }
            ),

            "party_size": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "max": 50,
                    "min":1,
                }
            ),

            "duration": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "max": 2,
                    "min": 1,
                }
            )
        }
        