from django.contrib import auth, messages
from django.contrib.auth import decorators
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.template.defaultfilters import first
from users.models import Tiket,ReplyTask,ReplyTiket,Task
from .inputs import olaviatha, vaziatha


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
    # replys = ReplyTiket.objects.filter(tiket=request.GET['id'])
    usergroup = str(user.groups.first())
    if usergroup == "admin" or usergroup == "programmers_admin":
        tikets = Tiket.objects.all()
    else:
        tikets = Tiket.objects.filter(user=request.user)
    # mode=0
    # if usergroup == "programmers":
    #     mode = 1
    # elif usergroup == "programmers_admin":
    #     mode = 2
    # elif usergroup == "admin":
    #     mode = 3
    #     queries = Tiket.objects.all()
    # elif usergroup == "customer":
    #     mode = 4

    
    context = {
        'user': user,
        #'mode': mode,
        'tikets':tikets,
        'vaziatha': vaziatha,
        'olaviatha': olaviatha,
    }
    return render(request, 'dashboard.html', context)


@login_required(login_url='login')
def newtiket(request):
    user = User.objects.get(pk=request.user.id)
    context = {
        'vaziatha': vaziatha,
        'olaviatha': olaviatha,
    }
    if request.method == 'POST':
        title = request.POST['title']
        olaviat = request.POST['olaviat']
        description = request.POST['description']
        post=Tiket(title=title,description=description,olaviat=olaviat,user=user)
        post.save()
    return render(request, 'dashboard.html',context=context)

@login_required(login_url='login')
def listing(request, listing_id):
    this_tiket=Tiket.objects.get(pk=listing_id)
    user = request.user
    # Return 404 error if no object found
    listing = get_object_or_404(Tiket, pk=listing_id)
    if ReplyTiket.objects.exists():
        replys = ReplyTiket.objects.filter(tiket=this_tiket)
    else:
        replys=None
    
    #get_object_or_404(Reply, pk=listing_id)

    if request.method == 'POST':
        if request.POST.get('change', False):
            u = this_tiket
            u.vaziat = request.POST['vaziat']
            u.save()
            return redirect('listing',listing_id)
        elif request.POST.get('submit', False):
            rmsg = request.POST['reply']
            p = ReplyTiket.objects.create(tiket=this_tiket, user=user, reply_message=rmsg)
    
    context = {
        'listing': listing,
        'replys': replys,
        'vaziatha': vaziatha
    }
    return render(request, 'listing.html',context=context)
