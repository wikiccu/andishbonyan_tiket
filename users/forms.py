from django import forms
from django.contrib.auth.models import User
from users.models import Task

class TasksForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Task
        fields = ['username', 'email']
