from django.db import models

# Create your models here.

class server(models.Model):
	sname = models.CharField(max_length=200, null=True)

	class Meta:
		db_table = 'serverlist'

	def __str__(self):
		return self.sname

class scheduleserver(models.Model):
	sername = models.CharField(max_length=200, null=True)
	start = models.CharField(max_length=10, null=True)
	stop = models.CharField(max_length=10, null=True)

	class Meta:
		db_table = 'scheduleserver'

	def __str__(self):
		return self.sername
