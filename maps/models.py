from django.db import models

# Create your models here.
class Categoria(models.Model):
	nome = models.CharField(blank=True, max_length=50)
	
	def __unicode__(self):
	        return self.nome
	
class Spot(models.Model):
	nome = models.CharField(max_length=50)
	categoria = models.ManyToManyField(Categoria)#, through='CategoriaSpot')
	foto = models.URLField()
	descricao = models.CharField(max_length=500)
	latitude = models.CharField(max_length=50)
	longitude = models.CharField(max_length=50)
	
	def __unicode__(self):
	        return self.nome

#class CategoriaSpot(models.Model):
#	categoria = models.ForeignKey(Categoria)
#	spot = models.ForeignKey(Spot)
