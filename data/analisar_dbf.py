# coding: utf-8

from dbf_rw import dbfreader
from pprint import pprint
from bz2 import BZ2File

ENCODING_DBF = 'cp1252'

class Campo(object):
    agregados = 'nome min max zero null blank mais_curto mais_longo'.split()
    def __init__(self, nome, tupla_tipo):
        self.nome = nome.lower()
        self.tipo = dict(N=int, C=unicode, F=float)[tupla_tipo[0]]
        self.larg = tupla_tipo[1]
        self.decimais = tupla_tipo[2]
        self.min = None
        self.max = None
        self.zero = False
        self.null = False
        self.blank = False
        self.mais_curto = None
        self.mais_longo = u''

    def checar(self, valor):
        if valor is None:
            self.null = True
            return # nada mais a fazer
        if self.tipo is unicode:
            valor = valor.decode(ENCODING_DBF).strip()
            if len(valor) == 0:
                self.blank = True
            if self.mais_curto is None or len(valor) < len(self.mais_curto):
                self.mais_curto = valor
            if len(valor) > len(self.mais_longo):
                assert len(valor) <= self.larg
                self.mais_longo = valor
        else:
            valor = self.tipo(valor)
            if valor == 0:
                self.zero = True
        if self.min is None or valor < self.min: 
            self.min = valor          
        if self.max is None or valor > self.max:
            self.max = valor

    def relatorio(self):
        atrs = Campo.agregados
        return [(atr, getattr(self, atr)) for atr in atrs]

def estatisticas():
    arq_dbf = BZ2File('BR_Localidades_2010_v1.dbf.bz2')
    localidades = dbfreader(arq_dbf)

    nomes = []
    tipos = []
    # ler dois primeiros registros para extrair a definicao dos campos
    for i, loc in enumerate(localidades):
        if i == 0:
            nomes = loc
        elif i == 1:
            tipos = loc
        else:
            break

    campos = [Campo(n, t) for n, t in zip(nomes, tipos)]

    for loc in localidades:
        for campo, valor in zip(campos, loc):
            campo.checar(valor)

    return campos

def relatorio(campos):

   #      1234567890 123456789012345 123456789012345
    print 'nome                   min             max zero null blank [curto] mais_longo'
    for campo in campos:
        stats = campo.__dict__.copy()
        stats['zero'] = '0' if stats['zero'] else '-'
        stats['null'] = 'N' if stats['null'] else '-'
        stats['blank'] = 'B' if stats['blank'] else '-'
        if stats['mais_curto'] is None: stats['mais_curto'] = '-'
        if campo.tipo is unicode:
            stats['min'] = stats['min'][:15]
            stats['max'] = stats['max'][:15]
        print u'{nome:10} {min:15} {max:15} {zero:^4} {null:^4} {blank:^5} [{mais_curto}] {mais_longo}'.format(**stats)


if __name__=='__main__':
    import pickle
    campos = estatisticas()
    pickle.dump(campos, open('campos.pickle','wb'))
    relatorio(campos)



