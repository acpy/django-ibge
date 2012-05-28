from .models import MesoRegiao, REGIOES

class Regiao(object):
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def to_dict(self):
        return self.__dict__

regioes = [Regiao(id_reg, nome) for id_reg, nome in REGIOES]

