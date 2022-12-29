from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name ='accounts'
urlpatterns = [
    path('', views.home_login, name='home_login_path'),
    path('welcomeback/', views.welcomeback, name='welcome_back_path'),
    path('register/', views.register, name='register_path'),
    path('login/', LoginView.as_view(), name='login_path'),
    path('logout/', LogoutView.as_view(next_page='accounts:home_login_path') ,name='logout_path'),

]
