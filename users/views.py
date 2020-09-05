from django.contrib import auth, messages
from django.contrib.auth import decorators
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.template.defaultfilters import first

from users.models import Reply

from .inputs import olaviatha, vaziatha
from .models import Inqueries


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
    queries = Inqueries.objects.filter(cuser=request.user)
    usergroup = str(user.groups.first())
    mode=0
    if usergroup == "programmers":
        mode = 1
    elif usergroup == "programmers_admin":
        mode = 2
    elif usergroup == "admin":
        mode = 3
        queries = Inqueries.objects.all()
    elif usergroup == "customer":
        mode = 4

    print(usergroup)
    print(mode)
    context = {
        'user': user,
        'mode': mode,
        'queries':queries,
    }
    return render(request, 'dashboard.html', context)


@login_required(login_url='login')
def newtiket(request):
    user = User.objects.get(pk=request.user.id)
    context = {
        'vaziatha': vaziatha,
        'olaviatha': olaviatha,
    }
    print(type(vaziatha))
    if request.method == 'POST':
        title = request.POST['title']
        olaviat = request.POST['olaviat']
        description = request.POST['description']
        post=Inqueries(title=title,description=description,olaviat=olaviat,cuser=user)
        post.save()
    return render(request, 'new_tiket.html',context=context)

@login_required(login_url='login')
def listing(request, listing_id):
    #inq=Inqueries.objects.get(pk=listing_id)
    #user = User.objects.get(pk=request.user.id)
    # Return 404 error if no object found
    listing = get_object_or_404(Inqueries, pk=listing_id)
    context = {
        'listing': listing,
    }
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']

    return render(request, 'listing.html',context=context)
