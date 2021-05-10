from datetime import datetime
from datetime import date 
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from DefaultSchedule import TaskScript

def start(serverid, opt):
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    if opt == 1 :
        exec_date = datetime(2021, 5, 10, 1, 15, 5)

    if opt == 2 :
        exec_date = datetime(2021, 5, 10, 1, 17, 5)

    scheduler.add_job(func = TaskScript.StartInstance, trigger = 'date', run_date = exec_date, args = [serverid])

    scheduler.start()

