from django.db import models
from django.contrib.auth.models import User, Group 

# Create your models here.

class server(models.Model):
	sname = models.CharField(max_length=200, null=True)
	InstID = models.CharField(max_length=200, null=True)
	user_grp = models.ManyToManyField(Group)
	class Meta:
		db_table = 'serverlist'

	def __str__(self):
		return self.sname


class requestdetail(models.Model):
	CHOICES = [('Y', 'Yes'), ('N', 'No')]
	sername = models.CharField(max_length=200, null=True)
	date = models.DateField(blank=True, null=True)
	start = models.TimeField(max_length=10, null=True)
	stop = models.TimeField(max_length=10, null=True)
	From = models.DateField(blank=True, null=True)
	To = models.DateField(blank=True, null=True)
	didItStart = models.CharField(max_length=1, choices = CHOICES, default = 'N') 
	didItStop = models.CharField(max_length=1, choices = CHOICES, default = 'N')
	scheduleFlag = models.IntegerField(default = 0)
	username = models.CharField(max_length=200, null=True)

	class Meta:
		db_table = 'requestdetail'

	def __str__(self):
		if self.sername : 
			return self.sername
		else : 
			return str(self.id)



class rds(models.Model):
	RDSname = models.CharField(max_length=200, null=True)
	date = models.DateField(blank=True, null=True)
	start = models.TimeField(max_length=10, null=True)
	stop = models.TimeField(max_length=10, null=True)
	From = models.DateField(blank=True, null=True)
	To = models.DateField(blank=True, null=True)

	class Meta:
		db_table = 'rds'

	def __str__(self):
		return self.RDSname


class test(models.Model):
	Testname = models.CharField(max_length=200, null=True)
	date = models.DateField(blank=True, null=True)
	start = models.TimeField(max_length=10, null=True)
	stop = models.TimeField(max_length=10, null=True)
	From = models.DateField(blank=True, null=True)
	To = models.DateField(blank=True, null=True)

	class Meta:
		db_table = 'test'

	def __str__(self):
		return self.Testname
