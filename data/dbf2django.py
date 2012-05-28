# coding: UTF-8

from dbf_rw import dbfreader
from pprint import pprint
from bz2 import BZ2File
from json import dump, dumps

arq_dbf = BZ2File('BR_Localidades_2010_v1.dbf.bz2')
entrada = dbfreader(arq_dbf)

nomes = []
tipos = []
localidades = []

# partes de nomes que devem ser em caixa baixa
CX_BAIXA = u'Da Das De Do Dos'
CX_BAIXA = [u' %s ' % p for p in CX_BAIXA.split()]

# expressoes que devem ser mantidas em CAIXA ALTA
CX_ALTA = u'AUI' # área urbana isolada

def caixa_mista(s):
    if s.upper() == CX_ALTA:
        return s.upper()
    s = s.title()
    for p in CX_BAIXA:
        s = s.replace(p, p.lower())
    return s

for i, loc in enumerate(entrada):
    if i == 0:
        nomes = [n.lower() for n in loc]
    elif i == 1:
        tipos = loc
    else:
        registro = dict(model='localidades.localidade')
        campos = {}
        for nome, tipo, valor in zip(nomes, tipos, loc):
            if valor is None:
                vi_none = True
            if nome == 'id':
                registro['pk'] = valor
                continue
            if nome == 'gmrotation':
                continue # ignorar este campo
            if tipo[0] == 'C':
                texto = valor.decode('cp1252')
                campos[nome] = caixa_mista(texto.strip())
            else:
                if valor is None:
                    valor = 0
                # dump JSON do Django representa numeros como strings
                campos[nome] = str(valor)
        registro['fields'] = campos
        localidades.append(registro)

with open('localidades.json','w') as arq_fixture:
    dump(localidades, arq_fixture, indent=2)
