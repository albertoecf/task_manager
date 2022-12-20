from django.shortcuts import render, redirect
from .models import taskModel
from .forms import taskForm
from django.contrib import messages


def home(request):

    if request.method == 'POST':
        form = taskForm(request.POST or None)
        if form.is_valid():
            print('form valid')
            form.save()
            all_items = taskModel.objects.all()
            messages.success(request, ("New item addedd.."))
            print(all_items)
            return render(request, 'index.html', {'all_items': all_items})
        else :
            print('invalid form')
            return render(request, 'index.html', {'all_items': 'Not valid form'})
    else:
        all_items = taskModel.objects.all()
        return render(request, 'index.html', {'all_items': all_items})

def delete(request, list_id):

    item = taskModel.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item deleted'))
    return redirect('home_path')
