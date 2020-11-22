from django.shortcuts import render,redirect,HttpResponse
from hotel_admin.adminform import *
from django.contrib import messages
from visitor.models import bookedRooms,user
from hotel_admin.models import *

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

def change_capacity(request):
    rooms = roomType.objects.all()
    return render(request, "admin/change_capacity.html", {'rooms': rooms, 'ad': admin_session(request)})

def save_capacity_room(request):
    d1 = request.POST.get('rm')
    d2 = request.POST.get('cp')
    d3 = request.POST.get('beds')
    data = roomType.objects.get(id=d1)
    data.capacity=d2
    data.beds = d3
    data.save()
    messages.success(request,"Capacity is updated")
    return redirect("change_capacity")

def bychin(request):
    return render(request,"admin/filterby_chin_date.html",{ 'ad': admin_session(request)})

def checkByChin(request):
    d1 = request.POST.get('chin')
    d2 = bookedRooms.objects.filter(checkin_date=d1)
    us = user.objects.all()
    rm = hotelRooms.objects.all()
    if d2:
        return render(request, "admin/filterby_chin_date.html", {'brooms':d2,'user':us,'room':rm,'ad': admin_session(request)})
    else:
        messages.success(request, "Sorry ..No Records")
        return redirect("bychin")

def fromchin(request):
    return render(request, "admin/filterfrom_chin_date.html", {'ad': admin_session(request)})

def checkfromchin(request):
    d1 = request.POST.get('chin')
    d2 = bookedRooms.objects.filter(checkin_date__gte=d1)
    us = user.objects.all()
    rm = hotelRooms.objects.all()
    if d2:
        return render(request, "admin/filterfrom_chin_date.html",
                  {'brooms': d2, 'user': us, 'room': rm, 'ad': admin_session(request)})
    else:
        messages.success(request, "Sorry ..No Records")
        return redirect("fromchin")

def fromandto(request):
    return render(request, "admin/filterfromandto.html", {'ad': admin_session(request)})

def checkfromandto(request):
    d1 = request.POST.get('chin')
    d2 = request.POST.get('chout')
    d3 = bookedRooms.objects.filter(checkin_date__gte=d1, checkout_date__lte=d2)
    us = user.objects.all()
    rm = hotelRooms.objects.all()
    if d3:
        return render(request, "admin/filterfromandto.html",
                  {'brooms': d3, 'user': us, 'room': rm, 'ad': admin_session(request)})
    else:
        messages.success(request, "Sorry ..No Records")
        return redirect("fromandto")

def byusername(request):
    return render(request, "admin/byuname.html", {'ad': admin_session(request)})

def checkbyusername(request):
    d1 = request.POST.get('nm')
    us = user.objects.filter(name=d1)
    d2 = bookedRooms.objects.filter(user__name=d1)
    rm = hotelRooms.objects.all()
    if d2:
        return render(request, "admin/byuname.html",
                  {'brooms': d2, 'user': us, 'room': rm, 'ad': admin_session(request)})
    else:
        messages.success(request,"Sorry ..No Records, Please provide proper username")
        return redirect("byusername")

def byroom(request):
    rooms = roomType.objects.all()
    return render(request, "admin/byroom.html", {'rooms':rooms,'ad': admin_session(request)})

def checkbyroom(request):
    d1 = request.POST.get('nm')
    us = user.objects.all()
    rooms = roomType.objects.all()
    rm = hotelRooms.objects.filter(type__id=d1)
    d2 = bookedRooms.objects.filter(roomId__type__id=d1)
    if d2:
        return render(request, "admin/byroom.html",
                      {'rooms':rooms,'brooms': d2, 'user': us, 'room': rm, 'ad': admin_session(request)})
    else:
        messages.success(request, "Sorry ..No Records")
        return redirect("byroom")

def admin_logout(request):
    del request.session['admin_session']
    return redirect('admin_login')
