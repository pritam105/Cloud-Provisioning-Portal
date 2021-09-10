from django.urls import path
from . import views

urlpatterns = [
    path('', views.insertserver, name = "home"),
    
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    path('request', views.scheduleRequest, name= "exemptS"),
    path('rds', views.scheduleRDS, name= "exemptRDS"),
    path('extend', views.Extend, name= "extend"),
    path('stopImmediate', views.stopImmediate, name= "stopImmediate")
]
