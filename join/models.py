from django.db import models

# Create your models here.
class Join(models.Model):
	email = models.CharField(max_length=250)
	name = models.CharField(max_length=250, null=True, blank=True)
	lastname = models.CharField(max_length=250)
	password = models.CharField(max_length=250)

	def __unicode__(self):
		return self.email