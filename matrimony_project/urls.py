"""matrimony_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('read2/',views.read2, name='read2'),
    path('delete2/<int:id>',views.delete2,name='delete2'),
    path('login/',views.login,name='login'),
    path('admind/',views.admind,name='admind'),
    path('admindash/',views.admindash,name='admindash'),
    path('adminuser/',views.adminuser,name='adminuser'),
    path('about/',views.about,name='about'),
    path('admindata/',views.admindata,name='admindata'),
    path('adminoffer/',views.adminoffer,name='adminoffer'),
    path('adminprofit/',views.adminprofit,name='adminprofit'),
    path('createoff/',views.createoff,name='createoff'),
    path('readoff/',views.readoff, name='readoff'),
    path('deleteoff/<int:id>',views.deleteoff,name='deleteoff'),
    path('profile2/',views.profile2,name='profile2'),
    path('profilematch/',views.profilematch,name='profilematch'), 
    path('profiledata1/',views.profiledata1,name='profiledata1'),
    path('membership/',views.membership,name='membership'), 
    path('offer/',views.offer,name='offer'),
    path('moneyback/',views.moneyback,name='moneyback'),
    path('payment/',views.payment,name='payment'),
    path('adminmail/<int:id>',views.admindmail,name='admindmail'),
    path('admindmail/<int:id>/send/', views.send_admin_mail, name='send_admin_mail'),
    path('adminuserdays/<int:id>',views.adminuserdays,name='adminuserdays'),
    path('displaydata/<int:id>',views.displaydata,name='displaydata'),
    path('toggle_status/<int:id>',views.toggle_status,name='toggle_status'),
    path('toggle_block/<int:id>',views.toggle_block,name='toggle_block'),
    path('toggle_unblock/<int:id>',views.toggle_unblock,name='toggle_unblock'),
    path('',include('myapp.urls')),    
]
