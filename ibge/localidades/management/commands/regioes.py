# coding: utf-8

import json

from django.core.management.base import BaseCommand, CommandError
from localidades.models import Localidade

from unicodedata import normalize

def remover_acentos(txt, codif='utf-8'):
    #utxt = txt.decode(codif)
    #assert isinstance(utxt, unicode)
    return normalize('NFKD', txt).encode('ASCII','ignore')

class Command(BaseCommand):
    args = '<campo>'
    help = u'Exportar municípios'

    def handle(self, *args, **options):
        distintos = set()
        mais_longo = u'' 
        for loc in Localidade.objects.all():
            if not loc.nm_meso:
                continue
            distintos.add((loc.cd_geocodm[:1], loc.uf(), loc.nm_meso))
            if len(loc.nm_municip) > len(mais_longo):
                mais_longo = loc.nm_meso
        export = []
        for i, campos in enumerate(sorted(distintos), 1):
            cod, uf, nome = campos
            reg = dict(pk=i, model='municipios.mesoregiao')
            reg['fields'] = dict(regiao=cod, uf=uf, nome=nome, nome_ascii=remover_acentos(nome))
            export.append(reg)
            #self.stdout.write(cod+' '+uf+' '+nome+'\n')
        #self.stdout.write('%s regioes\n' % len(distintos))
        self.stdout.write(json.dumps(export, indent=2))
