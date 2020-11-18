from django import forms
from HMSapp.models import BookingModel

class availForm(forms.Form):
    # class Meta:
    #     model= BookingModel
    #     fields='__all__'
    room_type = (
        ('Standard', 'Standard'),
        ('Deluxe', 'Deluxe'),
        ('Luxury', 'Luxury'),
        ('Sea facing', 'Sea facing'),
    )
    type = forms.ChoiceField(choices=room_type,required=True)
    checkin = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    checkout = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
