from django.shortcuts import render

def home_login(request):
    return render(request, 'loginpage.html')

def welcomeback(request):
    return render(request, 'welcomeback.html')
# Create your views here.
