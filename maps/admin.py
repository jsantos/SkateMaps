from skatemaps.maps.models import Categoria
from skatemaps.maps.models import Spot
from django.contrib import admin

class CategoriaAdmin(admin.ModelAdmin):
	fieldsets = [
		('Categoria', {'fields': ['nome']}),
	]
	list_display = ('nome',)
	#list_filter = ['pub_date']
	#search_fields = ['question']
	#date_hierarchy = 'pub_date'


admin.site.register(Categoria, CategoriaAdmin)

class SpotAdmin(admin.ModelAdmin):
	fieldsets = [
		('Geral', {'fields': ['nome', 'foto', 'descricao', 'categoria'], }),
		('Mapa', {'fields': ['latitude', 'longitude'], }),
	]
	
	list_display = ('nome', 'foto', 'descricao', 'latitude', 'longitude',)
	filter_horizontal = ('categoria', )
	
admin.site.register(Spot, SpotAdmin)	