# coding: utf-8

from django.db import models

from django.contrib.localflavor.br import br_states

REGIOES = [
    (1, u'Norte'),
    (2, u'Nordeste'),
    (3, u'Sudeste'),
    (4, u'Sul'),
    (5, u'Centro-Oeste'),
]

UFS = dict([(sigla, nome) for sigla, nome in br_states.STATE_CHOICES])

class Municipio(models.Model):
    uf = models.CharField(max_length=2, db_index=True,
                          choices=br_states.STATE_CHOICES)
    nome = models.CharField(max_length=64, db_index=True)
    nome_ascii = models.CharField(max_length=64, db_index=True)
    meso_regiao = models.ForeignKey('MesoRegiao')
    #capital = models.BooleanField(default=False)
    #latitude = models.FloatField(null=True)
    #longitude = models.FloatField(null=True)
    #geohash = models.CharField(max_length=16, blank=True, default='')

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
