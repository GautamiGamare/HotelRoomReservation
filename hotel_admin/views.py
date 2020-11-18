from django.shortcuts import render,redirect,HttpResponse
from hotel_admin.adminform import *
from django.contrib import messages

def admin_login(request):
    return render(request,"admin/login.html")

def admin_registration(request):
    return render(request, "admin/admin_registration.html",{'form':adminForm})

def save_admin_details(request):
    ps = adminForm(request.POST)
    if ps.is_valid():
        ps.save()
        messages.success(request,"Registration Successful")
        return redirect('admin_login')
    else:
        return render(request,"admin/admin_registration.html",{'form':ps})

def admin_welcome(request):
    email = request.POST.get('t1')
    password = request.POST.get('t2')
    try:
        ad = adminDetails.objects.get(email=email,password=password)
        request.session['admin_session'] = ad.id
        return render(request,"admin/admin_welcome.html",{'ad': ad})
    except adminDetails.DoesNotExist:
        messages.success(request,"Invalid Email ID or Password")
        return render(request,"admin/login.html")

def admin_session(request):
    adm = request.session['admin_session']
    admin = adminDetails.objects.get(id=adm)
    return admin

def add_rooms(request):
    return render(request, "admin/add_rooms.html", {'form': roomTypeForm, 'ad': admin_session(request)})

def save_room(request):
    ps = roomTypeForm(request.POST, request.FILES)
    if ps.is_valid():
        ps.save()
        messages.success(request, "Details saved successful")
        return redirect('add_rooms')
    else:
        return render(request, "admin/add_rooms.html", {'form': ps})

def add_room_details(request):
    return render(request, "admin/add_rooms_details.html", {'form': hotelRoomForm, 'ad': admin_session(request)})

def save_room_details(request):
    ps = hotelRoomForm(request.POST, request.FILES)
    if ps.is_valid():
        ps.save()
        messages.success(request, "Details saved successful")
        return redirect('add_room_details')
    else:
        return render(request, "admin/add_rooms_details.html", {'form': ps})

def add_images(request):
    return render(request, "admin/add_images.html", {'form': roomImagesForm, 'ad': admin_session(request)})

def save_room_images(request):
    ps = roomImagesForm(request.POST, request.FILES)
    if ps.is_valid():
        ps.save()
        messages.success(request, "Images saved successful")
        return redirect('add_images')
    else:
        return render(request, "admin/add_images.html", {'form': ps, 'ad': admin_session(request)})


def view_report(request):
    br = bookedRooms.objects.all()
    users = user.objects.all()
    return render(request, "admin/view_report.html", {'booking': br, 'user': users,
                                                      'ad': admin_session(request), 'room1': hotelRooms.objects.all()})


def filter_rooms(request):
    cin = request.POST.get('cin')
    cout = request.POST.get('cout')
    ty = request.POST.get('ty')
    nm = request.POST.get('uname')
    if (cin and cout and ty and nm):
        user1 = user.objects.filter(name=nm)
        for y in user1:
            b1 = bookedRooms.objects.filter(checkin_date__gte=cin, checkout_date__lte=cout, type=ty, user=y.id)
            if (b1):
                return render(request, "admin/filter_rooms.html",
                              {'booking': b1, 'user': user1, 'ad': admin_session(request),
                               'room1': hotelRooms.objects.all()})
        else:
            messages.success(request, "No Records")
            return render(request, "admin/filter_rooms.html",
                          {'ad': admin_session(request), 'room1': hotelRooms.objects.all()})
    elif (cin and cout and ty):
        b1 = bookedRooms.objects.filter(checkin_date__gte=cin, checkout_date__lte=cout, type=ty)
        if (b1):
            for x in b1:
                user1 = user.objects.filter(id=x.user)
                return render(request, "admin/filter_rooms.html",
                              {'booking': b1, 'user': user1, 'ad': admin_session(request),
                               'room1': hotelRooms.objects.all()})
        else:
            messages.success(request, "No Records")
            return render(request, "admin/filter_rooms.html",
                          {'ad': admin_session(request), 'room1': hotelRooms.objects.all()})
    elif (ty and nm):
        user1 = user.objects.filter(name=nm)
        if (user1):
            for x in user1:
                b1 = bookedRooms.objects.filter(user=x.id, type=ty)
                if (b1):
                    for y in b1:
                        return render(request, "admin/filter_rooms.html",
                                      {'booking': y, 'user': user1, 'ad': admin_session(request),
                                       'room1': hotelRooms.objects.all()})
                else:
                    messages.success(request, "No Records")
                    return render(request, "admin/filter_rooms.html",
                                  {'ad': admin_session(request), 'room1': hotelRooms.objects.all()})
        else:
            messages.success(request, "No Records")
            return render(request, "admin/filter_rooms.html",
                          {'ad': admin_session(request), 'room1': hotelRooms.objects.all()})
    elif (ty):
        b1 = bookedRooms.objects.filter(type=ty)
        if (b1):
            for x in b1:
                user1 = user.objects.filter(id=x.user)
                return render(request, "admin/filter_rooms.html",
                              {'booking': b1, 'ad': admin_session(request),
                               'room1': hotelRooms.objects.all(), 'user': user1, })
        else:
            messages.success(request, "No Records")
            return render(request, "admin/filter_rooms.html",
                          {'ad': admin_session(request), 'room1': hotelRooms.objects.all()})
    else:
        return HttpResponse("Please Give Proper Input")


def admin_logout(request):
    del request.session['admin_session']
    return redirect('admin_login')
