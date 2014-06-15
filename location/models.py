from django.db import models

# Create your models here.
class Location(models.Model):
	id_location = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=250)
	description = models.CharField(max_length=650)
	
	def __unicode__(self):
		return self.name

class Hotel(models.Model):
	id = models.IntegerField(primary_key=True)
	id_location = models.ForeignKey('Location')
	name = models.CharField(max_length=250)
	description = models.CharField(max_length=650)
	price = models.IntegerField()
	
	def __unicode__(self):
		return self.name

class Restaurants(models.Model):
	id = models.IntegerField(primary_key=True)
	id_location = models.ForeignKey('Location')
	name = models.CharField(max_length=350)
	description = models.CharField(max_length=650)
	price = models.IntegerField()
	
	def __unicode__(self):
		return self.name

class General(models.Model):
	id = models.IntegerField(primary_key=True)
	id_location = models.ForeignKey('Location')
	name = models.CharField(max_length=650)
	description = models.CharField(max_length=650)
	country = models.CharField(max_length=650)
	language = models.CharField(max_length=650)
	currency = models.CharField(max_length=650)
	visaReq = models.BooleanField(max_length=650)
	
	def __unicode__(self):
		return self.name

class Sport(models.Model):
	id = models.IntegerField(primary_key=True)
	id_location = models.ForeignKey('Location')
	name = models.CharField(max_length=650)
	description = models.CharField(max_length=650)
	
	def __unicode__(self):
		return self.name
