"""
URL configuration for hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.index), 
    path('blog/',views.blog),
    path('about/',views.about),
    path('contact/',views.contact),
    path('booking/',views.booking),
    path('service/',views.service),
    path('signup/',views.signup),
    path('signup_submit/',views.signup_button,name="form_submission"),
    path('login/',views.login),
    path('login_button/',views.login_button,name="login_submission"),
    path('logout/',views.logout),
    path('booking_button/',views.booking_button,name="booking_submission"),
    path('booking_confirm/',views.booking_confirm),
    path('admin_page/',views.admin_page),
    path('booking_cancel/',views.booking_cancel,name="booking_cancel"),
    path('admin_login_page/',views.admin_page),
    path('admin_login/',views.admin_login_submit,name="admin_login_submission"),
    path('bookings_admin/',views.admin_bookings),
    path('user_select/',views.user_select,name="user_select"),
    path('booking_approve/',views.booking_approve,name="booking_approve"),
    
]
