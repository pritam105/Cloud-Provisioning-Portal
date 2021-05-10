from django.urls import path
from . import views

urlpatterns = [
    path('', views.insertserver),
    path('request', views.scheduleRequest)
]
