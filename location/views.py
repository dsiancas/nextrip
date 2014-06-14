from django.shortcuts import render_to_response, RequestContext

from .models import Location, Hotels
from cart import Cart
from cart.models import Item

def location(request):
	results = Location.objects.all()
	return render_to_response('join/home.html',{'results': results},context_instance=RequestContext(request))

def detail(request):
	return render_to_response('location/location.html',locals(),context_instance=RequestContext(request))

#def add_cart(request, product_id, quantity, unit_price):
#    product = Hotels.objects.get(id=product_id)
#    cart = Cart(request)
#    cart.add(product, unit_price, quantity)

def add_cart(request):
    product = Hotels.objects.get(id=1)
    cart = Cart(request)
    cart.add(product, 10, 10)


def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)

def get_cart(request):
	return render_to_response('location/cart.html', dict(cart=Cart(request)))