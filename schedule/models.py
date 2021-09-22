from django.db import models
from django.contrib.auth.models import User, Group 

# Create your models here.

class server(models.Model):
	sname = models.CharField(max_length=200, null=True)

	class Meta:
		db_table = 'serverlist'

	def __str__(self):
		return self.sname


class scheduleserver(models.Model):
	sername = models.CharField(max_length=200, null=True)
	date = models.DateField(blank=True, null=True)
	start = models.TimeField(max_length=10, null=True)
	stop = models.TimeField(max_length=10, null=True)
	From = models.DateField(blank=True, null=True)
	To = models.DateField(blank=True, null=True)
	scheduleFlag = models.IntegerField(default = 0)
	user_grp = models.ManyToManyField(Group)

	class Meta:
		db_table = 'scheduleserver'

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
