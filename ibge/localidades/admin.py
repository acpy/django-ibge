from django.contrib import admin
from .models import Localidade

class LocalidadeAdmin(admin.ModelAdmin):
    list_display = ('uf', 'nm_meso', 'nm_micro', 'nm_municip', 
                    'nm_distrit', 'nm_subdist', 'nm_bairro', 
                    'nm_localid')
    list_display_links = list_display[:2]+list_display[-1:]
    search_fields = ('nm_municip',)
    list_filter = ('tipo', 'nm_uf', 'cd_nivel', 'nm_categor')

admin.site.register(Localidade, LocalidadeAdmin)
