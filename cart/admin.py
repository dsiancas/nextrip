from django.contrib import admin

from .models import Cart, Item

class CartAdmin(admin.ModelAdmin):
	class Meta:
		model = Cart

class ItemAdmin(admin.ModelAdmin):
	class Meta:
		model = Item

admin.site.register(Cart, CartAdmin)
admin.site.register(Item, ItemAdmin)