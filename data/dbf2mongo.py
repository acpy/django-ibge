from dbf_rw import dbfreader
from pprint import pprint
from bz2 import BZ2File
from json import dumps

arq_dbf = BZ2File('BR_Localidades_2010_v1.dbf.bz2')
localidades = dbfreader(arq_dbf)

nomes = []
tipos = []

for i, loc in enumerate(localidades):
    if i == 0:
        nomes = [n.lower() for n in loc]
    elif i == 1:
        tipos = loc
    else:
        registro = {}
        for nome, tipo, valor in zip(nomes, tipos, loc):
            if tipo[0] == 'C':
                registro[nome] = valor.decode('cp1252').strip()
            else:
                registro[nome] = valor
        print dumps(registro)

