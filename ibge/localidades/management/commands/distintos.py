# coding: utf-8

from django.core.management.base import BaseCommand, CommandError
from localidades.models import Localidade

class Command(BaseCommand):
    args = '<campo>'
    help = u'Exportar municípios'

    def handle(self, *args, **options):
        distintos = set()
        mais_longo = u'' 
        for loc in Localidade.objects.all():
            if not loc.nm_municip:
                continue
            distintos.add((loc.cd_geocodm, loc.uf(), loc.nm_municip))
            if len(loc.nm_municip) > len(mais_longo):
                mais_longo = loc.nm_municip

        for cod, uf, nome in sorted(distintos):
            self.stdout.write(cod+' '+uf+' '+nome+'\n')

        self.stdout.write('%s municípios\n' % len(distintos))
        self.stdout.write('nome mais longo: ')
        self.stdout.write('(%s) %s\n' % (len(mais_longo), mais_longo))
