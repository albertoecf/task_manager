from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home_login(request):
    return render(request, 'loginpage.html')

@login_required
def welcomeback(request):
    return render(request, 'welcomeback.html')
# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login_path')
    else :
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form':form})
