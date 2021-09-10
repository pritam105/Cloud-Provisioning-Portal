from datetime import datetime
from datetime import date 
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
#from DefaultSchedule import TaskScript

'''
def start(serverid, Datee, Hr, Minute):
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    exec_date = datetime(2021, 5, int(Datee), int(Hr), int(Minute), 5)
    
    #exec_date = datetime(2021, 5, 10, 1, 17, 5)

    scheduler.add_job(func = TaskScript.StartInstance, trigger = 'date', run_date = exec_date, args = [serverid], replace_existing = True)

    scheduler.start()

'''

def start(serverid, Datee, Hr, Minute):
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    exec_date = datetime(2021, 5, int(Datee), int(Hr), int(Minute), 5)
    
    #exec_date = datetime(2021, 5, 10, 1, 17, 5)

    scheduler.add_job(func = TaskScript.StartInstance, trigger = 'date', run_date = exec_date, args = [serverid], replace_existing = True)

    scheduler.start()
