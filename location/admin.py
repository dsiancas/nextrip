from django.contrib import admin

from .models import Location
from .models import Hotel, Restaurants, General, Sport

class LocationAdmin(admin.ModelAdmin):
	class Meta:
		model = Location

class HotelAdmin(admin.ModelAdmin):
	class Meta:
		model = Hotel

class RestaurantsAdmin(admin.ModelAdmin):
	class Meta:
		model = Restaurants

class GeneralAdmin(admin.ModelAdmin):
	class Meta:
		model = General

class SportAdmin(admin.ModelAdmin):
	class Meta:
		model = Sport


admin.site.register(Location, LocationAdmin)
admin.site.register(Sport, SportAdmin)
admin.site.register(General, GeneralAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Restaurants, RestaurantsAdmin)