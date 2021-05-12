from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from DefaultSchedule import updater

def insertserver(request):
    if request.method == "POST" :
        if request.POST.get('sname') :
            serverInstance = server()   #object of the table "server" in models.py
            serverInstance.sname = request.POST.get('sname')
            serverInstance.save()
            messages.success(request, 'The selected server '+ serverInstance.sname + ' is saved')
	    
        return render(request, 'index.html')

    else :
        return render(request, 'index.html')

def scheduleRequest(request) :
    results = server.objects.all()
    d = list(range(1,31))
    h = list(range(0,24))
    m = list(range(0,60))

    context = {'serverobj': results,
               'datee': d,
               'hr': h,
               'min': m
    }

    if request.method == "POST" :
        
        if request.POST.get('sername') :
            instance = scheduleserver()
            sn = request.POST.get('sername')
            instance.sername = sn 
            instance.save()

        if request.POST.get('startD') :
            updater.start(sn, request.POST.get('startD'), request.POST.get('startH'), request.POST.get('startM'))

        return render(request, 'scheduleRequest.html', context)
            
    else :         
        return render(request, 'scheduleRequest.html', context)
