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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Home.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('adminauthenticate/',authenticateadmin),
    path('admin/homepage/',adminhomepage, name = 'adminhomepage'),
    path('',homePage),
    path('hotels/',page2,),
    path('price/',price),
    path('add/',add),
    path('delete/<int:hotelpk>/',delete),
    path('signupuser/',signupuser),
    path('authenticate/',userauthenticate),
    path('customerwelcome/',customerwelcome),
    path('logoutuser/',logoutuser),
    path('book/<int:hotelp>/',book),
    path('userbookings/',userbooking),
    path('hotels/<int:hotelp>/',specifichotel),
    path('cancel/<int:bookid>/',cancel),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)