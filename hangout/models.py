from django.db import models

# Create your models here.

class Place(models.Model):
	name = models.CharField(max_length=30)
	intro = models.TextField()
	category = models.ManyToManyField('Category') 
	city = models.ForeignKey('City')
	address = models.CharField(max_length=200)
	allday = models.BooleanField()
	homepage = models.URLField()
	photo = models.ImageField(upload_to='static/hangout')


	def __str__(self):
		return self.name

class City(models.Model):
	name = models.CharField(max_length=30)
	country = models.CharField(max_length=30)
	language = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Visit(models.Model):
	place = models.ForeignKey('Place')
	date = models.DateField('Date visited')
	buddy = models.CharField(max_length=10)
	photo = models.ImageField(upload_to='static/hangout')
	comment = models.TextField()
	
	def __str__(self):
		return str(self.date)



