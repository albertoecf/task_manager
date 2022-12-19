from django.shortcuts import render
from .models import taskModel

def home(requests):

    all_items = taskModel.objects.all()

    return render(requests, 'index.html', {'all_items':all_items})
