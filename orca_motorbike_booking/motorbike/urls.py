from django.contrib import admin
from django.urls import path,include
from motorbike import views
from django.contrib.auth.views import *
urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
