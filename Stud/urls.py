"""Stud URL Configuration

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
from django.urls import include

from django.contrib.auth.views import LoginView, LogoutView

from .import views
from django.contrib import admin
from django.urls import path
from .import Hod_views, views
from django.conf import settings
from django.conf.urls.static import static
from .views import CustomPasswordResetView, CustomPasswordResetConfirmView, custom_password_reset_done, custom_password_reset_complete



urlpatterns = [

    path('admin', admin.site.urls),
    path('base', views.Base, name='base'),
    path('home', Hod_views.Home, name='home'),
    # path('foncier_home', Staff_views.Home, name='foncier_home'),
    # profile
    path('acceueil/', views.Accueil, name='acceueil'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', custom_password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', custom_password_reset_complete, name='password_reset_complete'),

    path('peche/', views.peche, name="peche"),
    path('post/<int:id>/', views.detail, name="detail"),
    path('post/', views.all, name="post"),
    path('new_post', views.new_post, name="new_post"),
    path('update_post/<int:pk>/', views.update_post, name="update_post"),
    path('delete_post/<int:id>/', views.delete_post, name="delete_post"),

    path('ressource/', views.ress, name="ressource"),
    path('upda_res/<int:id>/', views.upda_ress, name="upda_res"),
    path('delete_ress/<int:id>/', views.del_ress, name="delete_ress"),
    path('update_video/<int:id>/', views.update_vid, name="update_video"),
    path('delete_video/<int:id>/', views.delete_vid, name="delete_video"),
    path('b/', views.bl, name='b'),

    path('gestionnaire', views.coord, name='gestionnaire'),
    path('decideur', views.deci, name='decideur'),
    path('visiteur', views.visit, name='visiteur'),
    # end login
    path('profile_list/', views.profile_list, name='profile_list'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('profile_detail/', views.profile_detail, name='profile_detail'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
    path('commune', views.commune, name='commune'),
    path('commune_detail', views.co, name='commune_detail'),
    path('peche/', include('peche.urls')),
    path('r', views.re, name='r'),
	path('', views.teste, name='test'),
    path('com', views.come, name='com'),
    path('donne', views.donne, name='donne'),
    path('log', views.log, name='log'),
	
	path('atelier/', views.at, name='atelier'),
    path('upda_atl/<int:id>/', views.upda_atl, name="upda_atl"),
    path('delete_atl/<int:id>/', views.del_atl, name="delete_atl"),
    path('documt/', views.documt, name='documt'),
    path('upda_doc/<int:id>/', views.upda_doc, name="upda_doc"),
    path('delete_doc/<int:id>/', views.del_doc, name="delete_doc"),
    path('indi/', views.indict, name='indi'),
    path('upda_indi/<int:id>/', views.upda_i, name="upda_indi"),
    path('delete_indi/<int:id>/', views.del_i, name="delete_indi"),
    # diagramme

 


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
