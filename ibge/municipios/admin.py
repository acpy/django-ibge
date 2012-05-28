from django.contrib import admin
from .models import Municipio, MesoRegiao

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('pk', 'uf', 'nome')
    list_display_links = list_display
    search_fields = ('nome', 'nome_ascii',)
    list_filter = ('uf',)

class MesoRegiaoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'uf', 'nome')
    list_display_links = list_display
    search_fields = ('nome', 'nome_ascii',)
    list_filter = ('uf',)

admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(MesoRegiao, MesoRegiaoAdmin)
