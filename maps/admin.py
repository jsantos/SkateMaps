from skatemaps.maps.models import Categoria, Spot#, CategoriaSpot
from django.contrib import admin

class CategoriaAdmin(admin.ModelAdmin):
	fieldsets = [
		('Categoria', {'fields': ['nome']}),
	]
	list_display = ('nome',)
	
admin.site.register(Categoria, CategoriaAdmin)

class SpotAdmin(admin.ModelAdmin):
	fieldsets = [
		('Geral', {'fields': ['nome', 'foto', 'descricao', 'categoria'], }),
		('Mapa', {'fields': ['latitude', 'longitude'], }),
	]
	list_display = ('nome', 'foto', 'descricao', 'latitude', 'longitude')
	filter_horizontal = ('categoria', )
	
admin.site.register(Spot, SpotAdmin)	