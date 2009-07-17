# Create your views here.
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import render_to_response, get_object_or_404
from skatemaps.maps.models import *

def index(request):
	return render_to_response('index.html', {'spots': spots, 'user': request.user} )

def spots(request):
	spots = Spot.objects.all()
	return render_to_response('spots.html', {'spots': spots, 'user': request.user})

def spotdetail(request, spot_id):
	spot = get_object_or_404(Spot, pk=spot_id)
	return render_to_response('spotdetail.html', {'spot': spot, 'user': request.user})

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')		