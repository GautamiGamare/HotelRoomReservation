from django.contrib import admin
from django.urls import path
from visitor import views
from Hotel import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.show_main, name="index"),
    path('login/',views.login,name="login"),
    path('validate_user/',views.validate_user,name="validate_user"),
    path('registration/',views.registration,name="registration"),
    path('save_user_details/',views.save_user_details,name="save_user_details"),
    path('welcome_user/',views.welcome_user,name="welcome_user"),
    path('check_room_availb/',views.check_room_availb,name="check_room_availb"),
    path('book_room/',views.book_room,name="book_room"),
    path('confirm_booking/', views.confirm_booking, name="confirm_booking"),
    path('check_availability/',views.check_availability,name="check_availability"),
    path('cancel_booking/',views.cancel_booking,name="cancel_booking"),
    path('cancelB/',views.cancelB,name="cancelB"),
    path('user_logout/',views.user_logout,name="user_logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

