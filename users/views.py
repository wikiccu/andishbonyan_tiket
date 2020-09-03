from .inputs import olaviatha,vaziatha
from django.contrib import auth, messages
from django.contrib.auth import decorators
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.template.defaultfilters import first


def home(request):
  return render(request,"login.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            #messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'ورود با مشکل مواجه شد')
            return redirect('login')
    else:
        return render(request, 'login.html')

@login_required(login_url='login')
def dashboard(request):
    user = User.objects.get(pk=request.user.id)
    usergroup = str(user.groups.first())
    mode=0
    if usergroup == "programmers":
        mode = 1
    elif usergroup == "programmers_admin":
        mode = 2
    elif usergroup == "admin":
        mode = 3
    elif usergroup == "customer":
        mode = 4

    print(usergroup)
    print(mode)
    context = {
        'user': user,
        'mode': mode,
        'vaziatha': vaziatha,
        'olaviatha': olaviatha,
    }
    return render(request, 'dashboard.html', context)


@login_required(login_url='login')
def newtiket(request):
    context = {
        'vaziatha': vaziatha,
        'olaviatha': olaviatha,
    }
    if request.method == 'POST':
        title = request.POST['title']
        vaziat = request.POST['vaziat']
        olaviat = request.POST['olaviat']
        content = request.POST['content']
        print(title,vaziat,olaviat,content)

    return render(request, 'new_tiket.html',context=context)

