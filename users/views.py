from django.contrib import auth, messages
from django.contrib.auth import decorators
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.template.defaultfilters import first
from users.models import Tiket,ReplyTask,ReplyTiket,Task
from .inputs import olaviatha, vaziatha
from .forms import TasksForm

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
def dashboard(request ):
    user = User.objects.get(pk=request.user.id)
    usergroup = str(user.groups.first())
    show_tasks=True
    tikets = Tiket.objects.filter(vaziat="باز")
    if usergroup == "admin" or usergroup == "programmers_admin":
        if request.method == 'GET':
            if "close" == request.GET.get("q",False):
                tikets = Tiket.objects.filter(vaziat="بسته")
            elif "prog" == request.GET.get("q",False):
                tikets = Tiket.objects.filter(vaziat="در حال بررسی")
            else:
                tikets = Tiket.objects.filter(vaziat="باز")
                if 'new' == request.GET.get("q",False):
                    tikets=Tiket.objects.filter(vaziat="باز").order_by('-datetime')
                    print("new")
                elif 'old' == request.GET.get("q",False) :
                    tikets=Tiket.objects.filter(vaziat="باز").order_by('datetime')
                    print("old")

        show_tasks=True
    elif usergroup == "programmer":
        tikets = Tiket.objects.all()
        show_tasks=True
    else:
        tikets = Tiket.objects.filter(user=request.user)
        show_tasks=False
  
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
    if request.method == 'POST':
        title = request.POST['title']
        olaviat = request.POST['olaviat']
        description = request.POST['description']
        post=Tiket(title=title,description=description,olaviat=olaviat,user=user)
        post.save()
    
    context = {
        'user': user,
        #'mode': mode,
        'tikets':tikets,
        'vaziatha': vaziatha,
        'olaviatha': olaviatha,
        'show_tasks': show_tasks,
    }

    return render(request, 'dashboard.html',context=context)


    

@login_required(login_url='login')
def listing(request, listing_id):
    this_tiket=get_object_or_404(Tiket,pk=listing_id)
    user = request.user
    # Return 404 error if no object found
    listing = get_object_or_404(Tiket, pk=listing_id)
    if ReplyTiket.objects.exists():
        replys = ReplyTiket.objects.filter(tiket=this_tiket)
    else:
        replys=""
    
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

@login_required(login_url='login')
def tasks(request):
    tasks=None
    if request.method=="POST":
        form=TasksForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        if request.GET.get("t_s",False):
            t_s=request.GET["t_s"]
            t=get_object_or_404(Tiket,pk=t_s)
            tasks=t.task_set.all()
        else:
            if Task.objects.exists():
                tasks = Task.objects.all()
            else:
                tasks=None

        form=TasksForm(initial={'creator': request.user.get_full_name()})
    
    if request.user.groups.first().name == "customer":
        return redirect('dashboard')

    
        
        pass
    context = {
        'tasks':tasks,
        'form':form,
        #'vaziatha': vaziatha,
        #'olaviatha': olaviatha,
    }
    return render(request, 'tasks.html', context=context)

@login_required(login_url='login')
def tasksListing(request, listing_id):
    # Return 404 error if no object found
    listing = get_object_or_404(Task, pk=listing_id)
    # if ReplyTask.objects.exists():
    #     replys = ReplyTask.objects.filter(tiket=this_tiket)
    # else:
    #     replys=""
    
    #get_object_or_404(Reply, pk=listing_id)

    # if request.method == 'POST':
    #     if request.POST.get('change', False):
    #         u = this_tiket
    #         u.vaziat = request.POST['vaziat']
    #         u.save()
    #         return redirect('listing',listing_id)
    #     elif request.POST.get('submit', False):
    #         rmsg = request.POST['reply']
    #         p = ReplyTiket.objects.create(tiket=this_tiket, user=user, reply_message=rmsg)
    
    context = {
        'listing': listing,
        # 'replys': replys,
        'vaziatha': vaziatha
    }
    return render(request, 'taskslisting.html',context=context)
@login_required(login_url='login')
def tiketListing(request, tiketid):
    this_tiket=Tiket.objects.get(pk=tiketid)
    user = request.user
    # Return 404 error if no object found
    listing = get_object_or_404(Task, pk=tiketid)
    if ReplyTiket.objects.exists():
        replys = ReplyTiket.objects.filter(tiket=this_tiket)
    else:
        replys=""
    
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
    return render(request, 'taskslisting.html',context=context)
