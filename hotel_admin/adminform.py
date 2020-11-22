from django import forms
from hotel_admin.models import adminDetails ,hotelRooms,roomImages,roomType

class adminForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = adminDetails

    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)

class roomTypeForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = roomType

    typ = (('Standard', 'Standard'), ('Deluxe', 'Deluxe'), ('Sea facing suite', 'Sea facing suite'),
           ('Super Luxury', 'Super Luxury'))
    type = forms.ChoiceField(choices=typ)

    fclity = (('Wifi (2 devices per room)','Wifi (2 devices per room)'),('Partial ocean view','Partial ocean view'),
              ('Mini bar','Mini bar'),('Safe locker','Safe locker'),('Coffee/Tea maker','Coffee/Tea maker'),
              ('Bathrobe','Bathrobe'),('50.sq.mtrs','50.sq.mtrs'),('60.sq.mtrs','60.sq.mtrs'),
              ('35.sq.mtrs','35.sq.mtrs'),('32.sq.mtrs','32.sq.mtrs'),('King/Twin','King/Twin'),
              ('King','King'),('Cable/Satellite TV','Cable/Satellite TV'),('Bathtub','Bathtub'),('Hair Dryer','Hair Dryer'),
              ('News Paper','News Paper'),('Ocean view','Ocean view'))
    facility = forms.MultipleChoiceField(choices=fclity)


class hotelRoomForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = hotelRooms

class roomImagesForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = roomImages
