from django.urls import path
from .views import *

urlpatterns=[
    path('index/',index),
    path('register/',realestate_register),
    path('adminlogin/',admin_login),
    path('property_upload/',property_upload),
    path('property_disp/',property_disp),
    path('room_upload/<int:id>',room_upload),
    path('room_disp/<int:id>',room_disp),
    path('tenent_reg/',tenent_register),
    path('tenent_disp/',tenent_disp,),
    path('tenent_login/',tenent_login),
    path('customer_disp/',customer_disp),
    path('logout/',customer_logout),
    path('booking_reg/<int:id>',booking_reg),
    path('admin_disp/',admin_disp),
    path('prop_disp/',prop_disp),
    path('room_display/',admin_room_disp),
    path('edit/<int:id>',tenent_edit),
]