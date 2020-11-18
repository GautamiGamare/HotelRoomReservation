import datetime
from visitor.models import bookedRooms,user
from hotel_admin.models import roomType,hotelRooms,roomImages

def check_avail(room,checkin,checkout):
    avail_list = []
    booking_list =hotelRooms.objects.filter(room=room)
    for booking in booking_list:
        if ((booking.checkin > checkout ) or (booking.checkout < checkin)):
            avail_list.append(True)
            # print(avail_list)
        else:
            avail_list.append(False)
    return all(avail_list)
