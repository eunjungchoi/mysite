from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    intro = models.TextField()
    date = models.DateTimeField('date established')
    homepage = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='static/company')
    def __str__(self):
    	return "(" + str(self.id) + ")" + self.name


class People(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	position = models.CharField(max_length=30)
	def __str__(self):
		return "(" + str(self.id) + ")" + self.name

class Jobs(models.Model):
	title = models.CharField(max_length=50) 
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	position = models.CharField(max_length=30)
	jd = models.TextField()
	qualification = models.TextField()
	deadline = models.DateTimeField('application deadline')
	salary = models.CharField(max_length=20)
	def __str__(self):
		return "(" + str(self.id) + ")" + self.name