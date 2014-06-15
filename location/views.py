from django.shortcuts import render_to_response, RequestContext

from .models import Location, Hotel, General, Sport, Restaurants
from cart import Cart
from cart.models import Item

def home(request):
	results = Location.objects.all()
	return render_to_response('join/home.html',{'results': results},context_instance=RequestContext(request))

def detail(request, detail_id):
    general = General.objects.get(id_location=detail_id)
    sport = Sport.objects.get(id_location=detail_id)
    hotel = Hotel.objects.filter(id_location=detail_id)
    restaurant = Restaurants.objects.filter(id_location=detail_id)
    ctx = {'general': general,'sport': sport, 'hotel':hotel, 'restaurant':restaurant}
    return render_to_response('location/location.html',ctx,context_instance=RequestContext(request))

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