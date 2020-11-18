import datetime
from HMSapp.models import RoomModel,BookingModel

def check_avail(room,checkin,checkout):
    avail_list = []
    booking_list =BookingModel.objects.filter(room=room)
    for booking in booking_list:
        if ((booking.checkin > checkout ) and (booking.checkout < checkin)):
            avail_list.append(True)
            # print(avail_list)
        else:
            avail_list.append(False)
    return all(avail_list)
