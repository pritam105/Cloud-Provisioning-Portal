from datetime import datetime
from datetime import date, time, timedelta 
#from apscheduler.schedulers.background import BackgroundScheduler
#from django_apscheduler.jobstores import DjangoJobStore
from TaskScript import StartInstance, StopInstance
import mysql.connector
import boto3
ec2 = boto3.resource('ec2')
#ec2 = boto3.resource('ec2')
#from schedule import task
import sys
import os
import django
import time 
#sys.path.append('E:/DjangoProj/portal')
os.environ['DJANGO_SETTINGS_MODULE'] = 'portal.settings'
django.setup() 

# your imports, e.g. Django models
from schedule.models import *


def main() :
    weekdayFlag = 0
    weekendFlag = 0
    '''
    connection = mysql.connector.connect(host='localhost',
                                         database='trial',
                                         user='root',
                                         password='shawshankred')

    sql_select_Query = "select * from scheduleserver"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    #records = cursor.fetchall()
    '''
    startS = ['i-0a83c426a1a968abd', 'i-07cd4b1228a0928ef']
    
    #print(datetime.today().strftime("%A"))
    Hr_now = datetime.now().hour
    Min_now = datetime.now().minute
    timeNow = time(Hr_now, Min_now)

    if datetime.today().weekday() < 5:
        weekdayFlag = 1
        weekendFlag = 0
    else:  # 5 Sat, 6 Sun
        weekendFlag = 1
        weekdayFlag = 0  

    
    #if ((Hr_now > 22 or Hr_now < 9) and weekdayFlag) or weekendFlag :      
    #    print("inside if")
    
    #records = scheduleserver.objects.all()

    if datetime.now().time() < record.start :
        print("before time")
    #startS.extend(records)
    #print(startS)
    '''
    waiter = ec2.meta.client.get_waiter('instance_running')
    print("waiting")
    waiter.wait(InstanceIds = startS)
    print("wait over")
    '''
    '''
    res = ec2.describe_instances(InstanceIds = startS) 
    for i in res['Reservations'] :
        print(i['Instances'][0]['State']['Name'])
        #print(i)
    '''

    for instance in ec2.instances.all():
        print (instance.id , instance.state['Name'])

    
    #target_hr = records[5][2].seconds//3600
    #target_min = (records[5][2].seconds%3600)//60

 
    #if not records[5][4] is None :
        #print("None detected")

    yes = date.today() - timedelta(1)

    #print(date.today() < yes)
    
    #print(tp>records[5][2])
    # 0,  1,          2,     3,    4,    5,  6
    # ID, Servername, Start, Stop, From, To, Date
       
    '''   
    if weekdayFlag : 
        startTime = datetime.time(9, 00) 
        stopTime = datetime.time(22, 00) 

        if Hr_now == 9 :        # MORNING START TIME
            
            #List of instance IDs of all infra critical servers
            infraCritical = server.objects.filter(infraCritical = 1).values_list('InstID', flat = True)
            
            #List of all DB servers
            dbServers = server.objects.filter(startupSeq = "3001")
            
            #List of all Web/App servers
            webAppServers = server.objects.filter(startupSeq = ["4001", "4003", "4050"])

            dbIDStart = []           #List of db servers to be started
            dbIDStop = []
            webAppIDStart = []       #List of webApp servers to be started
            webAppIDStop = []

            for row in dbServers : 
                if row.ActiveStatus : 
                    if row.toShutDown and row.toStartUp :   #to start all the normal db servers 
                        dbIDStart.append(row.InstID)

                    elif row.toShutDown and not row.toStartUp :   #db servers that are always off (57)
                        dbIDStop.append(row.InstID)

                    elif not row.toShutDown and row.toStartUp :   #db servers that are always on (2)
                        dbIDStart.append(row.InstID)

            for row in webAppServers : 
                if row.ActiveStatus : 
                    if row.toShutDown and row.toStartUp :   #to start all the normal wA servers (153)
                        webAppIDStart.append(row.InstID)

                    elif row.toShutDown and not row.toStartUp :   #wA servers that are always off (57)
                        webAppIDStop.append(row.InstID)

                    elif not row.toShutDown and row.toStartUp :   #wA servers that are always on (9)
                        webAppIDStart.append(row.InstID)
                             
                
            StartInstance(infraCritical) 
            
            waiter = ec2.get_waiter('instance_running')
            waiter.wait(InstanceIds = infraCritical)
            infraStoppedFlag = 0
            
            # This means all the infra Critical Servers are up & running 

            StartInstance(dbIDStart)
            waiter.wait(InstanceIds = dbID)

            StartInstance(webAppIDStart)
            #waiter.wait(InstanceIds = webAppID) 

            StopInstance(webAppIDStop)
            StopInstance(dbIDStop)


        if Hr_now == 22 :           # NIGHT SHUTDOWN TIME

            #List of instance IDs of all infra critical servers
            #infraCritical = server.objects.filter(infraCritical = 1).values_list('InstID', flat = True)
            
            #List of all DB servers
            dbServers = server.objects.filter(startupSeq = "3001")
            
            #List of all Web/App servers
            webAppServers = server.objects.filter(startupSeq = "4000")

            dbIDStart = []           #List of db servers to be started
            dbIDStop = []
            webAppIDStart = []       #List of webApp servers to be started
            webAppIDStop = []

            for row in webAppServers : 
                if row.ActiveStatus : 
                    if row.toShutDown and row.toStartUp and str(row.stop) == '22:00:00' :   
                        #to start all the normal wA servers (153)
                        webAppIDStop.append(row.InstID)

                    elif row.toShutDown and not row.toStartUp and str(row.stop) == '22:00:00' :   
                        #wA servers that are always off (57)
                        webAppIDStop.append(row.InstID)

                    elif not row.toShutDown and row.toStartUp :   #wA servers that are always on (9)
                        webAppIDStart.append(row.InstID) 
                   
            for row in dbServers : 
                if row.ActiveStatus : 
                    if row.toShutDown and row.toStartUp and str(row.stop) == '22:00:00' :   
                        #to start all the normal db servers 
                        dbIDStop.append(row.InstID)

                    elif row.toShutDown and not row.toStartUp and str(row.stop) == '22:00:00' :   
                        #db servers that are always off (57)
                        dbIDStop.append(row.InstID)

                    elif not row.toShutDown and row.toStartUp :   #db servers that are always on (2)
                        dbIDStart.append(row.InstID)
            
            
            StopInstance(webAppIDStop)
            waiter.wait(InstanceIds = webAppID)

            StopInstance(dbID) 
            waiter.wait(InstanceIds = dbID)

            StartInstance(webAppIDStart)
            StartInstance(dbIDStart)


        if startTime < datetime.time.now() < stopTime : 
            for row in records : 
                if row.ActiveStatus : 

                    if (row.toStartUp and row.toShutDown)or(row.toStartUp == 0 and row.toShutDown == 1) : 
                        #This includes both normal servers and the servers which are always off
                        if row.scheduleFlag == 1 :
                            if date.today() == row.Date : 

                                if target_start_hr == Hr_now and target_start_min == Min_now :
                                    start.append(row.InstID)

                                if target_stop_hr == Hr_now and target_stop_min == Min_now :
                                    stop.append(row.InstID)
                                    row.scheduleFlag = 0 
                                    row.Date = None
                                    row.start = datetime.time(9, 00)
                                    row.stop = datetime.time(22, 00)

                                elif datetime.now().time() < row.start : 
                                    stop.append(row.InstID)   

                            elif row.Date > date.today() :      #Date is in future
                                if row.toStartUp == 0 and row.toShutDown == 1 : 
                                    stop.append(row.InstID)
                                else : 
                                    start.append(row.InstID)

                            elif row.Date < date.today() :      #Date has passed 
                                row.scheduleFlag = 0 
                                row.Date = None
                                row.start = datetime.time(9, 00)
                                row.stop = datetime.time(22, 00)           

                        elif row.scheduleFlag == 2 :
                            if row.From <= date.today() <= row.To : 
                                if target_start_hr == Hr_now and target_start_min == Min_now :
                                    start.append(row.InstID)

                                if target_stop_hr == Hr_now and target_stop_min == Min_now :
                                    stop.append(row.InstID)
                                    if row.To == date.today() :
                                        row.scheduleFlag = 0 
                                        row.Date = None
                                        row.start = datetime.time(9, 00)
                                        row.stop = datetime.time(22, 00)

                                elif datetime.now().time() < row.start : 
                                    stop.append(row.InstID)

                            elif row.From > date.today() :      #Date is in future
                                if row.toStartUp == 0 and row.toShutDown == 1 : 
                                    stop.append(row.InstID)
                                else : 
                                    start.append(row.InstID)

                            elif row.To < date.today() :
                                row.scheduleFlag = 0 
                                row.Date = None
                                row.start = datetime.time(9, 00)
                                row.stop = datetime.time(22, 00)

                        elif row.scheduleFlag == 0 :
                            #Servers which are always off
                            if row.toStartUp == 0 and row.toShutDown == 1 :
                                stop.append(row.InstID)
                            else :     
                                start.append(row.InstID)            


                    if row.toShutDown == 0 and row.toStartUp == 1 :     #these servers are always on 
                        start.append(row.InstID)                
                        #this will switch IC servers on if by mistake they're off
                        #this condition includes some servers other than IC too 
                    

    if ((Hr_now > 22 or Hr_now < 9) and weekdayFlag) or weekendFlag :   # if it is weekend or night
        target_start_hr = row.start.hour 
        target_start_min = row.start.minute

        for row in records : 
            if row.ActiveStatus : 

                if (row.toStartUp and row.toShutDown)or(row.toStartUp == 0 and row.toShutDown == 1) : 
                    #This includes both normal servers and the servers which are always off
                    if row.scheduleFlag == 1 :
                        if date.today() == row.Date : 

                            if target_start_hr == Hr_now and target_start_min == Min_now :
                                start.append(row.InstID)

                            if target_stop_hr == Hr_now and target_stop_min == Min_now :
                                stop.append(row.InstID)
                                row.scheduleFlag = 0 
                                row.Date = None
                                row.start = datetime.time(9, 00)
                                row.stop = datetime.time(22, 00)

                            elif datetime.now().time() < row.start : 
                                stop.append(row.InstID)        
                        else : 
                            stop.append(row.InstID)

                    elif row.scheduleFlag == 2 :
                        if row.From <= date.today() <= row.To : 
                            if target_start_hr == Hr_now and target_start_min == Min_now :
                                start.append(row.InstID)

                            if target_stop_hr == Hr_now and target_stop_min == Min_now :
                                stop.append(row.InstID)
                                if row.To == date.today() :
                                    row.scheduleFlag = 0 
                                    row.Date = None
                                    row.start = datetime.time(9, 00)
                                    row.stop = datetime.time(22, 00)

                            elif datetime.now().time() < row.start : 
                                stop.append(row.InstID) 
                        else : 
                            stop.append(row.InstID)
                            
                    elif row.scheduleFlag == 0 :    #server is not scheduled for weekend
                        stop.append(row.InstID)

                    elif row.scheduleFlag == 3 :    #extend server runtime
                        if date.today() == row.Date : 
                            if target_stop_hr == Hr_now and target_stop_min == Min_now :
                                stop.append(row.InstID) 
                
                if row.toShutDown == 0 and row.toStartUp == 1 :     #these servers are always on 
                    start.append(row.InstID)                
                    #this will switch IC servers on if by mistake they're off
                    #this condition includes some servers other than IC too 


                if row.toShutDown : 
                    if row.scheduleFlag == 1 :
                        if date.today() == row.Date : 
                            if target_stop_hr == Hr_now and target_stop_min == Min_now :
                                stop.append(row.InstID)
                                row.scheduleFlag = 0 
                                row.Date = None
                                row.start = datetime.time(9, 00)
                                row.stop = datetime.time(22, 00)

                            elif Hr_now < target_start_hr and Min_now < target_start_min : 
                                stop.append(row.InstID)     

                    elif row.scheduleFlag == 2 :
                        if row.From < date.today() < row.To : 
                            if target_stop_hr == Hr_now and target_stop_min == Min_now :
                                stop.append(row.InstID)
                                row.scheduleFlag = 0 
                                row.From = None
                                row.To = None
                                row.start = datetime.time(9, 00)
                                row.stop = datetime.time(22, 00)

                            elif Hr_now < target_start_hr and Min_now < target_start_min : 
                                stop.append(row.InstID)

                    elif row.scheduleFlag == 0 :    #server is not scheduled for weekend
                        stop.append(row.InstID)

#Call Start an Stop Instance functions and send the instance id list as parameters to them. 
    #StartInstance(startS) 
    #StopInstance(stopS)          

    if ((Hr_now > 22 or Hr_now < 9) and weekdayFlag) or weekendFlag : 
        
        defaultCheck(records) 

        if infraStoppedFlag == 0 :
            check statuses of all the DB & webApp instances and shutdown Infra servers(with toShutDown flag 1) if these statuses are stopped.
            rec = server.objects.filter(startupSeq = "4000" and "3000")
            for instance in rec :
                instance.InstID 

            for instance in ec2.instances.all():
                if instance.state['Name'] == 'running' : 
                    break 

            StopInstance() 
            infraStoppedFlag = 1 


def Wait_Verify(InstList):
    running = 0
    while(running != len(InstList)) :

        ########### Delay ###########

        res = ec2.describe_instances(InstanceIds = infraCritical)     
        for i in res['Reservations'] :
            if i['Instances'][0]['State']['Name'] == 'running' : 
                running +=1 


def defaultCheck(records) :
    startS = []
    stopS = []
    Hr_now = datetime.now().hour
    Min_now = datetime.now().minute 

    for row in records:
        #target_start_hr = row[2].seconds//3600
        #target_start_min = (row[2].seconds%3600)//60

        target_start_hr = row.start.hour 
        target_start_min = row.start.minute

        if row.ActiveStatus and target_start_hr == Hr_now and target_start_min == Min_now :  
            # Enter if start time is now 
            if not row.Date is None :           # Enter if the date column is filled (i.e not empty)
                if date.today() == row.Date :   # Enter if the date is today 
                    startS.append(row.InstID)

            elif not row.From is None and not row.To is None : # Enter if the from & to column is filled
                if row.From < date.today() < row.To :
                    startS.append(row.InstID)
        
        target_stop_hr = row.stop.hour
        target_stop_min = row.stop.minute 

        if row.ActiveStatus and target_stop_hr == Hr_now and target_stop_min == Min_now :  # Enter if stop time is now 
            if not row.Date is None :           # Enter if the date column is filled (i.e not empty)
                if date.today() == row.Date :   # Enter if the date is today 
                    stopS.append(row.InstID)

            elif not row.From is None and not row.To is None :
                if row.From < date.today() < row.To :
                    stopS.append(row.InstID)

    #Call Start an Stop Instance functions and send the instance id list as parameters to them. 
    StartInstance(startS) 
    StopInstance(stopS)
    '''
    startS = []
    stopS = []
    onFlag = 0 
    startFlag = 0
    stopFlag = 0
    #List of instance IDs of all infra critical servers
    infraCritical = server.objects.filter(infraCritical = 1).values_list('InstID', flat = True)
        
    req = requestdetail.objects.exclude(didItStart = 'Y', didItStop = 'Y', Date = datetime.today())
    once = req.filter(scheduleFlag = 1, Date = date.today())

    rec = once.objects.order_by('sername')
    key = []
    for i in rec : 
        if i.sername not in key : 
            key.append(i.sername)

    for row in key :
        startTime = min(rec.filter(sername = row).values_list('start', flat = True))
        stopTime = max(rec.filter(sername = row).values_list('stop', flat = True))
        
        instances = rec.filter(sername = row)

        for instance in instances :
            if instance.start == timeNow : 
                #Current time is the start time of this instance
                instance.didItStart = 'Y'
                #startS.append(instance.InstID)  
                startFlag = 1

            elif timeNow < instance.start : 
                if not checkIfYN(instances) :  #if any req does not have Y N (including current req)
                    #stopS.append(instance.InstID)
                    stopFlag = 1

            elif timeNow > instance.start : 


        for instance in instances :
            if instance.stop == timeNow : 
                #Current time is the stop time of this instance
                instance.didItStop = 'Y'  
                #Stop the instance if any of the other req has Y N 
                check = instances.exclude(id = instance.id)     # this is the request id
                if(not checkIfYN(check)) :
                    stopFlag = 1

             elif timeNow > instance.stop : 
                 if(not checkIfYN(check)) :
                    stopFlag = 1
                
        if stopFlag == 1 :
            stopS.append(server.objects.get(sname = row).InstID)
        elif startFlag == 1 : 
            startS.append(server.objects.get(sname = row).InstID)    
                
            if stopTime == timeNow :
                #Current time is the max start time among all the req for this instance
                stopS.append(instance.InstID)
                instance.scheduleFlag = 0 
                instance.Date = None
                instance.start = None
                instance.stop = None 

            if timeNow < str(instance.start) or timeNow > str(instance.stop) :
                #Current time is before or after the slot 
                stopS.append(instance.InstID)    

        elif row.start < datetime.now().time() < row.stop :
            #Current time is between the slot timings
            onFlag = 1     

    for row in records:
        #target_start_hr = row[2].seconds//3600
        #target_start_min = (row[2].seconds%3600)//60
        
        if row.Date == date.today() : 
            if target_start_hr == Hr_now and target_start_min == Min_now :  
                startS.append(row.InstID)
                row.didItStart = 'Y'

            if target_stop_hr == Hr_now and target_stop_min == Min_now :
                stopS.append(row.InstID)
                row.scheduleFlag = 0 
                row.Date = None
                row.start = None
                row.stop = None 

            elif datetime.now().time() < row.start or datetime.now().time() > row.stop: 
                #Current time is before or after the slot 
                stopS.append(row.InstID)    

            elif row.start < datetime.now().time() < row.stop :
                #Current time is between the slot timings
                onFlag = 1 
                    
        elif row.Date < date.today() :    #Date is in the past : 
            row.Date = None
            stopS.append(row.InstID)

        elif row.Date > date.today() :    #Date is in the future : 
            stopS.append(row.InstID)        

        elif row.scheduleFlag == 2 :
            if row.From <= date.today() <= row.To :
                if target_start_hr == Hr_now and target_start_min == Min_now :  
                    startS.append(row.InstID)

                if target_stop_hr == Hr_now and target_stop_min == Min_now :
                    stopS.append(row.InstID)
                    row.scheduleFlag = 0 
                    row.Date = None
                    row.start = None
                    row.stop = None 

                elif datetime.now().time() < row.start or datetime.now().time() > row.stop: 
                    #Current time is before or after the slot 
                    stopS.append(row.InstID) 

            elif row.Date < date.today() :    #Date is in the past : 
                row.Date = None
                stopS.append(row.InstID)

            elif row.Date > date.today() :    #Date is in the future : 
                stopS.append(row.InstID)        

        if len(startS) != 0 :
            StartInstance(infraCritical) 
            waiter = ec2.get_waiter('instance_running')
            waiter.wait(InstanceIds = infraCritical)

            StartInstance(startS)
        else : 
            StopInstance(stopS)    
        StopInstance(stopS)

def checkIfYN(check) :
    for c in check : 
        if c.didItStart == 'Y' and c.didItStop == 'N' :
            return True 
    return False    


if __name__ == "__main__" :
    main()