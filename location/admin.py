from django.contrib import admin

from .models import Location

class LocationAdmin(admin.ModelAdmin):
	class Meta:
		model = Location

admin.site.register(Location, LocationAdmin)