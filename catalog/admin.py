from django.contrib import admin
from .models import Catalogo

@admin.register(Catalogo)
class CatalogoAdmin(admin.ModelAdmin):
    list_display = ('nombre_catalogo', 'especie', 'genero')
    list_filter = ['genero']


    #search_fields = [f.name for f in Catalogo._meta.fields]
    #list_per_page = 10


