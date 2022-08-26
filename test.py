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

Hr_now = datetime.now().hour
Min_now = datetime.now().minute
timeNow = time(Hr_now, Min_now)

rows = requestdetail.objects.all()

for row in rows :
    if row.start > timeNow :
        print("yes")