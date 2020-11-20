from django.shortcuts import render,redirect,HttpResponse
from hotel_admin.models import *
from passlib.hash import pbkdf2_sha256
from django.contrib import messages
from visitor.models import user,bookedRooms
import datetime


def show_main(request):
    room1 = roomType.objects.all()
    return render(request,"visitor/index.html",{'room1':room1})

def login(request):
    return render(request, "visitor/login.html")

def validate_user(request):
    em = request.POST.get('email')
    pas = request.POST.get('pass')
    try:
        qs = user.objects.get(email=em)
        pbkdf2_sha256.verify(pas, qs.password)
        request.session['user_session'] = qs.id
        ses = request.session['user_session']
        return render(request, "visitor/welcome_user.html",
                      {'ses': ses, 'roomd': bookedRooms.objects.filter(user=ses).order_by('-checkin_date'), 'user': user.objects.get(id=ses)})
    except user.DoesNotExist:
        messages.success(request, "Username or passoword is incorrect")
        return redirect(login)

def registration(request):
    return render(request, "visitor/registration.html")

def save_user_details(request):
    nm = request.POST.get('t1')
    num = request.POST.get('t2')
    email = request.POST.get('t3')
    pas = request.POST.get('t4')
    encrpt_password = pbkdf2_sha256.hash(pas)
    user(name=nm, contact_number=num, email=email, password=encrpt_password).save()
    messages.success(request, "Registration Successful")
    return redirect(login)

def facility(request,room_type):
    room = roomType.objects.get(type=room_type)
    def facility():
        f = room.facility
        ch = ["'", "[", "]"]
        list = ("".join(i for i in f if not i in ch)).rsplit(',')
        return list
    fac = facility()
    return fac

def check_room_availb(request):
    type = request.GET.get('room_type')
    room = roomType.objects.get(type=type)
    fac = facility(request,type)
    return render(request,"visitor/check_room.html",
                  {'images':roomImages.objects.filter(id=room.id),
                           'img1':room.images,'facility': fac,'cap':room.capacity,'room':room})

def welcome_user(request):
    ses = request.session['user_session']
    return render(request, "visitor/welcome_user.html",
                  {'ses': ses, 'roomd': bookedRooms.objects.filter(user=ses).order_by('-checkin_date'), 'user': user.objects.get(id=ses),
                   'type':hotelRooms.objects.all()})

def check_availability(request):
    rtype = request.POST.get('type')
    checkin = request.POST.get('cin')
    c1 = datetime.datetime.strptime(checkin,'%Y-%m-%d')
    cin = c1.replace(hour=12,minute=00,second=00)
    checkout = request.POST.get('cout')
    c2 = datetime.datetime.strptime(checkout, '%Y-%m-%d')
    cout = c2.replace(hour=11, minute=00, second=00)
    guest = request.POST.get('total_guest')
    rooms = request.POST.get('total_rooms')
    qs = hotelRooms.objects.filter(type__type=rtype)
    room = roomType.objects.get(type=rtype)
    fac = facility(request, rtype)
    if(len(qs) >= int(rooms)):
        bs = bookedRooms.objects.filter(roomId__type__type= rtype)
        if(bs):
            alist = avail_list(request, rtype, cin, cout)
            if(len(alist)>= int(rooms)):
                messages.success(request, "rooms are available")
                return render(request, "visitor/check_room.html",
                              {'images': roomImages.objects.filter(id=room.id),
                               'img1': room.images, 'facility': fac, 'cap': room.capacity, 'room': room,
                               'checkin': checkin, 'checkout': checkout, 'guest': guest, 'total_rooms': rooms})

            else:
                return render(request, "visitor/check_room.html",
                                  {'images': roomImages.objects.filter(id=room.id),
                                   'img1': room.images, 'facility': fac, 'cap': room.capacity, 'room': room,
                                   'msg': 'Rooms are not available'})


        else:
            messages.success(request, "rooms are available")
            return render(request, "visitor/check_room.html",
                          {'images': roomImages.objects.filter(id=room.id),
                           'img1': room.images, 'facility': fac, 'cap': room.capacity, 'room': room,
                           'checkin':checkin,'checkout':checkout,'guest':guest,'total_rooms':rooms})

    else:
        return render(request, "visitor/check_room.html",
                      {'images': roomImages.objects.filter(id=room.id),
                       'img1': room.images, 'facility': fac, 'cap': room.capacity, 'room': room,'msg':'Rooms are not available'})


def book_room(request):
    ses = request.session['user_session']
    cin = request.POST.get('cin')
    cout = request.POST.get('cout')
    ty = request.POST.get('ty')
    gst = request.POST.get('guest')
    rooms = request.POST.get('rooms')
    return render(request, "visitor/book_room.html", {'user':user.objects.get(id=ses),'cin': cin, 'cout': cout, 'ty': ty,'gst':gst,'rooms':rooms })

def confirm_booking(request):
    ses = request.session['user_session']
    us = user.objects.get(id=ses)
    cin = request.POST.get('cin')
    c1 = datetime.datetime.strptime(cin,'%Y-%m-%d')
    chin = c1.replace(hour=12,minute=00,second=00)
    cout = request.POST.get('cout')
    c2 = datetime.datetime.strptime(cout, '%Y-%m-%d')
    chout = c2.replace(hour=11, minute=00, second=00)
    ty = request.POST.get('ty')
    rooms = request.POST.get('rooms')
    iroom = int(rooms)
    alist = avail_list(request,ty,chin,chout)
    for a in range(iroom):
        hs = hotelRooms.objects.get(id=alist[a])
        booking = bookedRooms.objects.create(
            user=us,
            roomId=hs,
            checkin_date=cin,
            checkout_date=cout,
            rooms = 1,
            )
        booking.save()
    return render(request, "visitor/welcome_user.html",
              {'ses': ses, 'roomd': bookedRooms.objects.filter(user=ses).order_by('-checkin_date'),
               'user': us,'type':hotelRooms.objects.all()})

def avail_list(request,ty,chin,chout):
    bs = bookedRooms.objects.filter(roomId__type__type=ty)
    hs = hotelRooms.objects.filter(type__type=ty)
    avail_list = []
    rlist = []
    clist = []
    if (bs):
        for x in bs:
            for y in hs:
                hotel_room = int(y.id)
                booked_room = int(x.roomId_id)
                if (hotel_room == booked_room):
                    iin = datetime.datetime.combine(
                        datetime.date(x.checkin_date.year, x.checkin_date.month, x.checkin_date.day),
                        datetime.time(x.checkin_time.hour, x.checkin_time.minute))
                    out = datetime.datetime.combine(
                        datetime.date(x.checkout_date.year, x.checkout_date.month, x.checkout_date.day),
                        datetime.time(x.checkout_time.hour, x.checkout_time.minute))

                    if (iin > chout or out < chin):
                        pass
                    else:
                        if y.id not in clist:
                            clist.append(y.id)

                if y.id not in rlist:
                    rlist.append(y.id)
        for s in rlist:
            if s not in clist:
                avail_list.append(s)
        return avail_list
    else:
        hs = hotelRooms.objects.filter(type__type=ty)
        for y in hs:
            if y.id not in avail_list:
                avail_list.append(y.id)
        return avail_list

def cancel_booking(request):
    ses = request.session['user_session']
    us = user.objects.get(id=ses)
    ps = bookedRooms.objects.get(id=request.POST.get('cid'))
    hs = hotelRooms.objects.get(id=ps.roomId_id)
    room = roomType.objects.get(type=hs.type)
    return render(request,"visitor/cancel.html",{'user':us,'booking':ps,'hotel':hs,'room':room})

def cancelB(request):
    id = request.POST.get('bid')
    bookedRooms.objects.get(id=id).delete()
    return redirect('welcome_user')

def user_logout(request):
    del request.session['user_session']
    return redirect(login)