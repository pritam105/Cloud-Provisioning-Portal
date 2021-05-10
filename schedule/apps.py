from django.apps import AppConfig


class ScheduleConfig(AppConfig):
    name = 'schedule'
'''
    def ready(self):
        from DefaultSchedule import updater 
        updater.start()
'''
