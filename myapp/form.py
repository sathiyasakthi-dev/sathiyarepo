from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'status']

class TaskFilterForm(forms.Form):
    priority = forms.ChoiceField(choices=Task.PRIORITY_CHOICES, required=False)
    status = forms.ChoiceField(choices=Task.STATUS_CHOICES, required=False)
