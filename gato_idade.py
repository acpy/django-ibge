'''

    >>> felix = Gato('Felix')
    >>> felix.nome
    'Felix'
    >>> felix.idade
    0
    >>> print felix
    Felix (0)
    >>> felix.idade = 5
    Traceback (most recent call last):
      ...
    AttributeError: can't set attribute

'''

from datetime import date

class Gato(object):

    def __init__(self, nome, dt_nasc=None):
        self.nome = nome
        if dt_nasc is None:
            self.dt_nasc = date.today()

    @property
    def idade(self):
        if self.dt_nasc == date.today():
            return 0
        raise NotImplementedError

    def __str__(self):
        return '%s (%s)' % (self.nome, self.idade)


