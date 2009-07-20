# Create your views here.
from django.http import *
from django.contrib.auth import logout
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator
from skatemaps.maps.models import *

def index(request):
	return render_to_response('index.html', {'spots': spots, 'user': request.user} )

def spots(request, page):
	paginator = Paginator(Spot.objects.all(), 3)
	p = paginator.page(page)		
	spots = p.object_list
	return render_to_response('spots.html', {
		'show_paginator': paginator.num_pages > 1,
		'has_prev': p.has_previous(),
		'has_next': p.has_next(),
		'page': int(page),
		'pages': paginator.page_range,
		'prev': p.previous_page_number(),
		'next': p.next_page_number(),
 		'spots': spots,
		'user': request.user,
	})

def spotdetail(request, spot_id):
	spot = get_object_or_404(Spot, pk=spot_id)
	return render_to_response('spotdetail.html', {'spot': spot, 'user': request.user})

def spotmap(request, spot_id):
	spot = get_object_or_404(Spot, pk=spot_id)
	return render_to_response('spotmap.html', {'spot': spot, 'user': request.user})
	
def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')		