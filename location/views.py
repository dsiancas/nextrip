from django.shortcuts import render_to_response, RequestContext

from .models import Location

def location(request):
	return render_to_response('location/location.html',locals(),context_instance=RequestContext(request))