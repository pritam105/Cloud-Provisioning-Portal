from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_select2.forms import Select2MultipleWidget
from django import forms

from .models import *

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class YourCreateForm(forms.Form):
	CHOICES =  [tuple([x,x]) for x in server.objects.values_list('sname', flat = True)]
	server_name = forms.MultipleChoiceField(widget = Select2MultipleWidget, choices = CHOICES)
	#CHOICES = [('orange', 'Orange'), ('red', 'Red')] 
	#server_n = forms.CharField(widget = forms.Select(choices = CHOICES))
	#server_n = forms.ChoiceField(widget=forms.Select, choices = CHOICES)