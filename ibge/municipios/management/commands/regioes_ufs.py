from django.core.management.base import BaseCommand, CommandError
from municipios.models import Municipio

from pprint import pformat

class Command(BaseCommand):
    args = ''
    help = 'Gera listagem de UFs por regiao'

    def handle(self, *args, **options):
        regioes = set()
        for muni in Municipio.objects.all():
            regiao = int(str(muni.pk)[0])
            regioes.add( (regiao, muni.uf) )

        self.stdout.write(pformat(sorted(regioes)))

