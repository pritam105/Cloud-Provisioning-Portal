from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from DefaultSchedule import updater
from TaskScript import StartInstance, StopInstance

from datetime import datetime
from datetime import date, time, timedelta 

from .forms import CreateUserForm, YourCreateForm
from .decorators import unauthenticated_user, allowed_users, admin_only, Dynamic_Display

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')
        

    context = {'form':form}
    return render(request, 'register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')  
def insertserver(request):
    if request.method == "POST" :
        if request.POST.get('sname') :
            serverInstance = server()   #object of the table "server" in models.py
            serverInstance.sname = request.POST.get('sname')
            serverInstance.save()
            messages.success(request, 'The selected server '+ serverInstance.sname + ' is saved')
	    
        if request.POST.get('rds') :
            RDSInstance = rds()   #object of the table "server" in models.py
            RDSInstance.RDSname = request.POST.get('rds')
            RDSInstance.save()
            messages.success(request, 'The selected server '+ RDSInstance.RDSname + ' is saved')
	    
        return render(request, 'index.html')

    else :
        return render(request, 'index.html')

@login_required(login_url='login')
#@allowed_users(allowed_roles=['requestor', 'admin'])   
@Dynamic_Display
def scheduleRequest(request, *args, **kwargs) :

    #print(args)
    context = {'serverobj': args}

    if request.method == "POST" :
        
        #instance = scheduleserver.objects.get(sername = request.POST.get('sername'))
        instance = requestdetail()

        if request.POST.get('date') :
            '''
            if datetime.Parse(request.POST.get('date')) < date.today()  : 
                messages.success(request, 'Please enter a valid Date!')
            '''
            instance.scheduleFlag = 1
            instance.sername = request.POST.get('sername')
            instance.date = request.POST.get('date')
            instance.start = request.POST.get('start')
            instance.stop = request.POST.get('stop')
            instance.From = None
            instance.To = None
            instance.username = request.user.username 
            instance.save()
            messages.success(request, 'The schedule request for "'+ instance.sername + '" is submitted')

        if request.POST.get('From') :
            instance.scheduleFlag = 2
            instance.sername = request.POST.get('sername')
            instance.start = request.POST.get('start')
            instance.stop = request.POST.get('stop')
            instance.From = request.POST.get('From')
            instance.To = request.POST.get('To')
            instance.date = None
            instance.save()
            messages.success(request, 'The schedule request for "'+ instance.sername + '" is submitted')

        return render(request, 'scheduleRequest.html', context)
            
    else :         
        return render(request, 'scheduleRequest.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['requestor', 'admin'])   
def scheduleRDS(request) :
    results = rds.objects.all()
    context = {'rdsobj': results}

    if request.method == "POST" :
        
        instance = rds()

        if request.POST.get('date') :
            '''
            if request.POST.get('date') < date.today()  : 
                messages.success(request, 'Please enter a valid Date!')
            '''
            
            instance.date = request.POST.get('date')
            instance.start = request.POST.get('start')
            instance.stop = request.POST.get('stop')
            instance.save()

        if request.POST.get('RDSname') :
            sn = request.POST.get('RDSname')
            instance.RDSname = sn 
            instance.save()

        if request.POST.get('From') :
            instance.start = request.POST.get('start')
            instance.stop = request.POST.get('stop')
            instance.From = request.POST.get('From')
            instance.To = request.POST.get('To')
            instance.save()
        
        '''
        if request.POST.get('startD') :
            
            updater.start(sn, request.POST.get('startD'), request.POST.get('startH'), request.POST.get('startM'))
        '''
        return render(request, 'scheduleRDS.html', context)
            
    else :         
        return render(request, 'scheduleRDS.html', context)

@login_required(login_url='login')
@Dynamic_Display   
def Extend(request) : 
    
    context = {'serverobj': args}

    if request.method == "POST" :
        
        instance = scheduleserver.objects.get(sername = request.POST.get('sername'))

        if request.POST.get('date') :

            instance.date = request.POST.get('date')
            instance.stop = request.POST.get('stop')
            instance.save()
            messages.success(request, 'The extend request for "'+ instance.sername + '" is submitted')
        
        return render(request, 'extend.html', context)
            
    else :         
        return render(request, 'extend.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['requestor', 'admin'])   
def stopImmediate(request) :
    form = YourCreateForm()
    if request.method == "POST" :

        form = YourCreateForm(request.POST)
        if form.is_valid() :  
            stoplist = form.cleaned_data['server_n']
            messages.success(request, 'Your request for Immediate Server Stop has been submitted')
            StopInstance(stoplist)
    '''
    else : 
        name = 'chatbot'
        form = YourCreateForm(initial={'server_n': name})
    '''
    context = { 'form': form }

    return render(request, 'stopImmediate.html', context)





def roundTime(tim) : 
    hr = int(tim[:2])
    min = int(tim[3:])
    if (min > 30) :
        hr +=1 
        hr = hr%24
        return(str(hr) + ":" + "00")

    elif(min < 30) :
        min = 30  
        return(str(hr) + ":" + str(min))
    else :      
        return(tim)
