from django.contrib import admin

from .models import Location
from .models import Hotels, Restaurant

class LocationAdmin(admin.ModelAdmin):
	class Meta:
		model = Location

class HotelAdmin(admin.ModelAdmin):
	class Meta:
		model = Hotels

class RestaurantAdmin(admin.ModelAdmin):
	class Meta:
		model = Restaurant


admin.site.register(Location, LocationAdmin)
admin.site.register(Hotels, HotelAdmin)
admin.site.register(Restaurant, RestaurantAdmin)