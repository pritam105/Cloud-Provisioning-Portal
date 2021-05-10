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
    
    if request.method == "POST" :
        if request.POST.get('sername') :
            instance = scheduleserver()
            instance.sername = request.POST.get('sername')
            instance.save()

        if request.POST.get('start') :
            instance.start = request.POST.get('start')
            instance.save()

        if request.POST.get('stop') :
            instance.stop = request.POST.get('stop')
            instance.save()

        if request.POST.get('choice') == '1' :
            updater.start("i-07a2fc035f39f3c7e", 1)
            
        if request.POST.get('choice') == '2' :
            updater.start("i-0081f9a95017d789b", 2)    

        return render(request, 'scheduleRequest.html', {'serverobj': results})
            
    else :         
        return render(request, 'scheduleRequest.html', {'serverobj': results})
