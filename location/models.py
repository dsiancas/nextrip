from django.db import models

# Create your models here.
class Location(models.Model):
	id_location = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=250)
	description = models.CharField(max_length=650)
	price = models.IntegerField()

	def __unicode__(self):
		return self.id_location