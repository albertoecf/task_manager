from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_login, name='home_login_path'),
    path('welcomeback/', views.welcomeback, name='welcome_back_path'),

]
