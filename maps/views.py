# Create your views here.
from django.http import *
from django.shortcuts import render_to_response, get_object_or_404
from skatemaps.maps.models import *

def index(request):
	return render_to_response('index.html', {'spots': spots} )

def spots(request):
	spots = Spot.objects.all()
	return render_to_response('spots.html', {'spots': spots})

def spotdetail(request, spot_id):
	spot = get_object_or_404(Spot, pk=spot_id)
	return render_to_response('spotdetail.html', {'spot': spot})	