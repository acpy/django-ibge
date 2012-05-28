
import pickle

from analisar_dbf import Campo

campos = pickle.load(open('campos.pickle')) 

CABECALHO = '''\
from django.db import models

class Localidade(models.Model):'''

print CABECALHO

for campo in campos:
    if campo.nome in ['id', 'gmrotation']: 
        continue # ignorar estes campos
    params = [('db_index', True)]
    if campo.tipo is unicode:
        model_field ='CharField'
        params.append(('max_length', campo.larg))
        if campo.blank:
            params.append(('blank', True))
    else:
        model_field ='DecimalField'
        params.append(('max_digits', campo.larg))
        params.append(('decimal_places', campo.decimais))

    if campo.null:
        params.append(('null', True))
    params = ', '.join([nome+'='+repr(valor) for nome, valor in params])
    print '    {} = models.{}({})'.format(campo.nome, model_field, params)