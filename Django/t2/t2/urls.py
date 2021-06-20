"""t1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.contrib.auth import authenticate
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Home.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', adminloginview),
    path('adminauthenticate/',authenticateadmin),
    path('admin/homepage/',adminhomepage, name = 'adminhomepage'),
    path('',homePage),
    path('hotels/',page2,),  # ,name="list"
    path('hotel/',page3),
    path('silver_hotel/',page4),
    path('home/',redirecthomePage),
    path('price/',price),
    path('add/',add),
    path('delete/<int:hotelpk>/',delete),
    path('signupuser/',signupuser),
    path('authenticate/',userauthenticate),
    path('customerwelcome/',customerwelcome),
    # path('userlogout/',redirecthomePage),
    path('logoutuser/',logoutuser),
    path('book/<int:hotelp>/',book),
    path('userbookings/',userbooking),
    path('hotels/<int:hotelp>/',specifichotel),

    path('image_upload/', hotel_image_view, name = 'image_upload'),
    # path('admin/homepage/', hotel_image_view, name = 'imagee_upload'),
    path('success', success, name = 'success'),
    path('hotel_images/', display_hotel_images, name = 'hotel_images')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)