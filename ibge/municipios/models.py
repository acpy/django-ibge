# coding: utf-8

from django.db import models

from django.contrib.localflavor.br import br_states

UFS = dict([(sigla, nome) for sigla, nome in br_states.STATE_CHOICES])

REGIOES = [
    (1, u'Norte'),
    (2, u'Nordeste'),
    (3, u'Sudeste'),
    (4, u'Sul'),
    (5, u'Centro-Oeste'),
]

REGIOES_UFS = [
    (1, u'AC'),
    (1, u'AM'),
    (1, u'AP'),
    (1, u'PA'),
    (1, u'RO'),
    (1, u'RR'),
    (1, u'TO'),
    (2, u'AL'),
    (2, u'BA'),
    (2, u'CE'),
    (2, u'MA'),
    (2, u'PB'),
    (2, u'PE'),
    (2, u'PI'),
    (2, u'RN'),
    (2, u'SE'),
    (3, u'ES'),
    (3, u'MG'),
    (3, u'RJ'),
    (3, u'SP'),
    (4, u'PR'),
    (4, u'RS'),
    (4, u'SC'),
    (5, u'DF'),
    (5, u'GO'),
    (5, u'MS'),
    (5, u'MT')
]

class Municipio(models.Model):
    uf = models.CharField(max_length=2, db_index=True,
                          choices=br_states.STATE_CHOICES)
    nome = models.CharField(max_length=64, db_index=True)
    nome_ascii = models.CharField(max_length=64, db_index=True)
    meso_regiao = models.ForeignKey('MesoRegiao')
    capital = models.BooleanField(default=False)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    geohash = models.CharField(max_length=16, blank=True, default='')

    class Meta:
        verbose_name = u'Município'
        verbose_name_plural = u'Municípios'
        ordering = ['nome_ascii']

    def __unicode__(self):
        return u'%s, %s' % (self.nome, self.uf)

class MesoRegiao(models.Model):
    uf = models.CharField(max_length=2, db_index=True,
                          choices=br_states.STATE_CHOICES)
    regiao = models.PositiveIntegerField(choices=REGIOES, db_index=True)
    nome = models.CharField(max_length=62, db_index=True)
    nome_ascii = models.CharField(max_length=62, db_index=True)

    class Meta:
        verbose_name = u'Meso Região'
        verbose_name_plural = u'Meso Regiões'
        ordering = ['nome_ascii']

    def __unicode__(self):
        return u'%s, %s' % (self.nome, self.uf)
