from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_path'),
    path('delete/<list_id>',views.delete, name='delete'),

]
