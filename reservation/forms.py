from django import forms
from .models import ReservationRequest


class ReservationRequestForm(forms.ModelForm):
    class meta:
        model = ReservationRequest
        fields =[
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "date",
            "time",
            "party_size",
            "boat",
            "duration",
        ]

