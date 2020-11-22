from django.urls import path,include
from hotel_admin import views
from Hotel import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.admin_login,name="admin_login"),
    path('admin_registration/',views.admin_registration,name="admin_registration"),
    path('save_admin_details/',views.save_admin_details,name="save_admin_details"),
    path('admin_welcome/',views.admin_welcome,name="admin_welcome"),
    path('add_rooms/',views.add_rooms,name="add_rooms"),
    path('save_room/',views.save_room,name="save_room"),
    path('add_room_details/',views.add_room_details,name="add_room_details"),
    path('save_room_details/',views.save_room_details,name="save_room_details"),
    path('change_capacity/',views.change_capacity,name="change_capacity"),
    path('save_capacity_room/',views.save_capacity_room,name="save_capacity_room"),
    path('add_images/',views.add_images,name="add_images"),
    path('save_room_images/',views.save_room_images,name="save_room_images"),
    path('bychin/',views.bychin,name="bychin"),
    path('checkByChin/',views.checkByChin,name="checkByChin"),
    path('fromchin/',views.fromchin,name="fromchin"),
    path('checkfromchin/',views.checkfromchin,name="checkfromchin"),
    path('fromandto/',views.fromandto,name="fromandto"),
    path('checkfromandto/',views.checkfromandto,name="checkfromandto"),
    path('byusername/',views.byusername,name="byusername"),
    path('checkbyusername/',views.checkbyusername,name="checkbyusername"),
    path('byroom/',views.byroom,name="byroom"),
    path('checkbyroom/', views.checkbyroom, name="checkbyroom"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
