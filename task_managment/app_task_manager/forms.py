from django import forms
from .models import taskModel

class taskForm(forms.ModelForm):
    class Meta:
        model = taskModel
        fields = ['task_name','priority_level']
