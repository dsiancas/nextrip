from django.db import models

# Create your models here.
class Location(models.Model):
	id_location = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=250)
	description = models.CharField(max_length=650)
	
	def __unicode__(self):
		return self.name

class Hotels(models.Model):
	id_hotel = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=250)
	description = models.CharField(max_length=650)
	price = models.IntegerField()
	
	def __unicode__(self):
		return self.name

class Restaurant(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=250)
	description = models.CharField(max_length=650)
	price = models.IntegerField()
	
	def __unicode__(self):
		return self.name