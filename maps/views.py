# Create your views here.
from django.http import HttpResponse
from skatemaps.maps.models import Categoria

def index(request):
	categories = Categoria.objects.all()
	output = ', '.join([c.nome for c in categories])
	return HttpResponse(output)