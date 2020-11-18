from django.urls import path
app_name='HMSapp'
from HMSapp import views

urlpatterns = [
    path('bookingList/',views.bookingList.as_view(),name="bookingList"),
    path('roomList/',views.roomList.as_view(),name="roomList"),
    path('book/',views.avail_room.as_view(),name="book"),
]