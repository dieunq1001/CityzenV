"""CityzenV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static

from CityzenV import settings
from CityzenV_app import views, admin_view, a1_view, a2_view, a3_view, b1_view, b2_view

urlpatterns = [
    path('', views.ShowLoginPage, name='show_login'),
    path('admin/', admin.site.urls),
    path('doLogin', views.DoLogin, name='do_login'),
    path('doLogout', views.DoLogOut, name='do_logout'),

    #admin
    path('admin_home', admin_view.admin_home, name='admin_home'),
    path('add_a1', admin_view.add_a1, name='admin_add_a1'),
    path('add_a1_save', admin_view.add_a1_save, name='admin_add_a1_save'),

    #a1
    path('a1_home', a1_view.a1_home, name='a1_home'),
    path('add_a2', a1_view.add_a2, name='a1_add_a2'),
    path('add_a2_save', a1_view.add_a2_save, name='a1_add_a2_save'),
    path('manage_cong_dan', a1_view.manage_cong_dan, name='a1_manage_cong_dan'),

    #a2
    path('a2_home', a2_view.a2_home, name='a2_home'),
    path('add_a3', a2_view.add_a3, name='a2_add_a3'),
    path('add_a3_save', a2_view.add_a3_save, name='a2_add_a3_save'),
    path('a2_manage_cong_dan', a2_view.a2_manage_cong_dan, name='a2_manage_cong_dan'),

    #a3
    path('a3_home', a3_view.a3_home, name='a3_home'),
    path('add_b1', a3_view.add_b1, name='a3_add_b1'),
    path('add_b1_save', a3_view.add_b1_save, name='a3_add_b1_save'),
    path('a3_manage_cong_dan', a3_view.a3_manage_cong_dan, name='a3_manage_cong_dan'),

    #b1
    path('b1_home', b1_view.b1_home, name='b1_home'),
    path('add_b2', b1_view.add_b2, name='b1_add_b2'),
    path('add_b2_save', b1_view.add_b2_save, name='b1_add_b2_save'),
    path('b1_add_cong_dan', b1_view.b1_add_cong_dan, name='b1_add_cong_dan'),
    path('b1_add_cong_dan_save', b1_view.b1_add_cong_dan_save, name='b1_add_cong_dan_save'),
    path('b1_manage_cong_dan', b1_view.b1_manage_cong_dan, name='b1_manage_cong_dan'),
    path('b1_edit_cong_dan/<str:congdan_id>', b1_view.b1_edit_cong_dan, name='b1_edit_cong_dan'),
    path('b1_edit_cong_dan_save', b1_view.b1_edit_cong_dan_save, name='b1_edit_cong_dan_save'),

    #b2
    path('b2_home', b2_view.b2_home, name='b2_home'),
    path('add_cong_dan', b2_view.add_cong_dan, name='b2_add_cong_dan'),
    path('add_cong_dan_save', b2_view.add_cong_dan_save, name='b2_add_cong_dan_save'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
