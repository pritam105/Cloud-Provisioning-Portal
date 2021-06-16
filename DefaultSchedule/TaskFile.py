from datetime import datetime
from datetime import date, time, timedelta 
#from apscheduler.schedulers.background import BackgroundScheduler
#from django_apscheduler.jobstores import DjangoJobStore
from TaskScript import StartInstance, StopInstance
import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='trial',
                                         user='root',
                                         password='shawshankred')

    sql_select_Query = "select * from scheduleserver"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    startS = []
    stopS = []
    Hr_now = datetime.now().hour
    Min_now = datetime.now().minute 

    target_hr = records[5][2].seconds//3600
    target_min = (records[5][2].seconds%3600)//60

    if not records[5][4] is None :
        print("None detected")

    yes = date.today() - timedelta(1)

    print(date.today() < yes)
    
    #print(tp>records[5][2])
    # 0,  1,          2,     3,    4,    5,  6
    # ID, Servername, Start, Stop, From, To, Date
    
    for row in records:
        target_start_hr = row[2].seconds//3600
        target_start_min = (row[2].seconds%3600)//60

        if target_start_hr == Hr_now and target_start_min == Min_now :  # Enter if start time is now 
            if not row[6] is None :           # Enter if the date column is filled (i.e not empty)
                if date.today() == row[6] :   # Enter if the date is today 
                    startS.append(row[1])

            elif not row[4] is None and not row[5] is None : # Enter if the from & to column is filled
                if row[4] < date.today() < row[5] :
                    startS.append(row[1])
        
        target_stop_hr = row[3].seconds//3600
        target_stop_min = (row[3].seconds%3600)//60

        if target_stop_hr == Hr_now and target_stop_min == Min_now :  # Enter if stop time is now 
            if not row[6] is None :           # Enter if the date column is filled (i.e not empty)
                if date.today() == row[6] :   # Enter if the date is today 
                    stopS.append(row[1])

            elif not row[4] is None and not row[5] is None :
                if row[4] < date.today() < row[5] :
                    stopS.append(row[1])

#Call Start an Stop Instance functions and send the instance id list as parameters to them. 
              


except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")