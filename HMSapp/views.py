from django.shortcuts import render,HttpResponse
from django.views.generic import ListView,FormView
from HMSapp.models import RoomModel,BookingModel
from HMSapp.form import availForm
from HMSapp.booking_function.check_availability import check_avail

class roomList(ListView):
    model = RoomModel
    template_name = "roomList.html"

class bookingList(ListView):
    model = BookingModel
    template_name = "bookingList.html"

class avail_room(FormView):
    form_class = availForm
    template_name = "avail.html"

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = RoomModel.objects.filter(type=data['type'])
        avail_list = []
        for room in room_list:
            if check_avail(room,data['checkin'],data['checkout'],data['checkin_time'],):
                avail_list.append(room)
                # print(avail_list)

        if len(avail_list) > 0:
            room = avail_list[0]
            booking = BookingModel.objects.create(
                user=self.request.user,
                room=room,
                checkin=data['checkin'],
                checkout=data['checkout']
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('All this category of rooms are booked')
