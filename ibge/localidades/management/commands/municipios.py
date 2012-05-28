# coding: utf-8

import json

from django.core.management.base import BaseCommand, CommandError
from localidades.models import Localidade

from unicodedata import normalize

MESO_REGIOES = {
    u'Agreste Alagoano': 21,
    u'Agreste Paraibano': 43,
    u'Agreste Pernambucano': 47,
    u'Agreste Potiguar': 56,
    u'Agreste Sergipano': 60,
    u'Araraquara': 85,
    u'Ara\xe7atuba': 86,
    u'Assis': 87,
    u'Baixadas': 79,
    u'Baixo Amazonas': 9,
    u'Bauru': 88,
    u'Borborema': 44,
    u'Campinas': 89,
    u'Campo das Vertentes': 67,
    u'Central Esp\xedrito-Santense': 63,
    u'Central Mineira': 68,
    u'Central Potiguar': 57,
    u'Centro Amazonense': 3,
    u'Centro Fluminense': 80,
    u'Centro Goiano': 124,
    u'Centro Maranhense': 38,
    u'Centro Norte Baiano': 24,
    u'Centro Norte de Mato Grosso do Sul': 129,
    u'Centro Ocidental Paranaense': 100,
    u'Centro Ocidental Rio-Grandense': 110,
    u'Centro Oriental Paranaense': 101,
    u'Centro Oriental Rio-Grandense': 111,
    u'Centro Sul Baiano': 25,
    u'Centro-Norte Piauiense': 52,
    u'Centro-Sul Cearense': 31,
    u'Centro-Sul Mato-Grossense': 133,
    u'Centro-Sul Paranaense': 102,
    u'Distrito Federal': 123,
    u'Extremo Oeste Baiano': 26,
    u'Grande Florian\xf3polis': 117,
    u'Itapetininga': 90,
    u'Jaguaribe': 32,
    u'Jequitinhonha': 69,
    u'Leste Alagoano': 22,
    u'Leste Goiano': 125,
    u'Leste Maranhense': 39,
    u'Leste Potiguar': 58,
    u'Leste Rondoniense': 15,
    u'Leste Sergipano': 61,
    u'Leste de Mato Grosso do Sul': 130,
    u'Litoral Norte Esp\xedrito-Santense': 64,
    u'Litoral Sul Paulista': 91,
    u'Macro Metropolitana Paulista': 92,
    u'Madeira-Guapor\xe9': 16,
    u'Maraj\xf3': 10,
    u'Mar\xedlia': 93,
    u'Mata Paraibana': 45,
    u'Mata Pernambucana': 48,
    u'Metropolitana de Belo Horizonte': 70,
    u'Metropolitana de Bel\xe9m': 11,
    u'Metropolitana de Curitiba': 103,
    u'Metropolitana de Fortaleza': 33,
    u'Metropolitana de Porto Alegre': 112,
    u'Metropolitana de Recife': 49,
    u'Metropolitana de Salvador': 27,
    u'Metropolitana de S\xe3o Paulo': 94,
    u'Metropolitana do Rio de Janeiro': 81,
    u'Nordeste Baiano': 28,
    u'Nordeste Mato-Grossense': 134,
    u'Nordeste Paraense': 12,
    u'Nordeste Rio-Grandense': 113,
    u'Noroeste Cearense': 34,
    u'Noroeste Esp\xedrito-Santense': 65,
    u'Noroeste Fluminense': 82,
    u'Noroeste Goiano': 126,
    u'Noroeste Paranaense': 104,
    u'Noroeste Rio-Grandense': 114,
    u'Noroeste de Minas': 71,
    u'Norte Amazonense': 4,
    u'Norte Catarinense': 118,
    u'Norte Cearense': 35,
    u'Norte Central Paranaense': 105,
    u'Norte Fluminense': 83,
    u'Norte Goiano': 127,
    u'Norte Maranhense': 40,
    u'Norte Mato-Grossense': 135,
    u'Norte Piauiense': 53,
    u'Norte Pioneiro Paranaense': 106,
    u'Norte de Minas': 72,
    u'Norte de Roraima': 17,
    u'Norte do Amap\xe1': 7,
    u'Ocidental do Tocantins': 19,
    u'Oeste Catarinense': 119,
    u'Oeste Maranhense': 41,
    u'Oeste Paranaense': 107,
    u'Oeste Potiguar': 59,
    u'Oeste de Minas': 73,
    u'Oriental do Tocantins': 20,
    u'Pantanais Sul Mato-Grossense': 131,
    u'Piracicaba': 95,
    u'Presidente Prudente': 96,
    u'Ribeir\xe3o Preto': 97,
    u'Serrana': 120,
    u'Sert\xe3o Alagoano': 23,
    u'Sert\xe3o Paraibano': 46,
    u'Sert\xe3o Pernambucano': 50,
    u'Sert\xe3o Sergipano': 62,
    u'Sert\xf5es Cearenses': 36,
    u'Sudeste Mato-Grossense': 136,
    u'Sudeste Paraense': 13,
    u'Sudeste Paranaense': 108,
    u'Sudeste Piauiense': 54,
    u'Sudeste Rio-Grandense': 115,
    u'Sudoeste Amazonense': 5,
    u'Sudoeste Mato-Grossense': 137,
    u'Sudoeste Paraense': 14,
    u'Sudoeste Paranaense': 109,
    u'Sudoeste Piauiense': 55,
    u'Sudoeste Rio-Grandense': 116,
    u'Sudoeste de Mato Grosso do Sul': 132,
    u'Sul Amazonense': 6,
    u'Sul Baiano': 29,
    u'Sul Catarinense': 121,
    u'Sul Cearense': 37,
    u'Sul Esp\xedrito-Santense': 66,
    u'Sul Fluminense': 84,
    u'Sul Goiano': 128,
    u'Sul Maranhense': 42,
    u'Sul de Roraima': 18,
    u'Sul do Amap\xe1': 8,
    u'Sul/Sudoeste de Minas': 74,
    u'S\xe3o Francisco Pernambucano': 51,
    u'S\xe3o Jos\xe9 do Rio Preto': 98,
    u'Tri\xe2ngulo Mineiro/Alto Parana\xedba': 75,
    u'Vale S\xe3o-Franciscano da Bahia': 30,
    u'Vale do Acre': 1,
    u'Vale do Itaja\xed': 122,
    u'Vale do Juru\xe1': 2,
    u'Vale do Mucuri': 76,
    u'Vale do Para\xedba Paulista': 99,
    u'Vale do Rio Doce': 77,
    u'Zona da Mata': 78
}

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
            if not loc.nm_municip:
                continue
            meso_regiao = MESO_REGIOES[loc.nm_meso]
            distintos.add((loc.cd_geocodm, loc.uf(), loc.nm_municip, meso_regiao))
            if len(loc.nm_municip) > len(mais_longo):
                mais_longo = loc.nm_municip
        export = []
        for cod, uf, nome, meso_regiao in sorted(distintos):
            reg = dict(pk=int(cod), model='municipios.municipio')
            reg['fields'] = dict(uf=uf, meso_regiao=meso_regiao,
                    nome=nome, nome_ascii=remover_acentos(nome))
            export.append(reg)

        self.stdout.write(json.dumps(export, indent=2))
