from django import forms
from django.contrib.auth.models import User
from django.forms.models import ModelChoiceField

from users.models import Tiket,Task


class TasksForm(forms.ModelForm):
    tiket = ModelChoiceField(queryset=Tiket.objects.all() ,label="تیکت")
    user = ModelChoiceField(queryset=User.objects.filter(groups__name="programmers") ,label="کاربر مجری")
    class Meta:
        model = Task
        fields = ['tiket', 'user','creator','task_message']
