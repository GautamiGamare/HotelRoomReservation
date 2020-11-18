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
    # path('change_capacity/',views.change_capacity,name="change_capacity"),
    # path('save_capacity_room/',views.save_capacity_room,name="save_capacity_room"),
    path('add_images/',views.add_images,name="add_images"),
    path('save_room_images/',views.save_room_images,name="save_room_images"),
    path('view_report/',views.view_report,name="view_report"),
    path('filter_rooms/',views.filter_rooms,name="filter_rooms"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
