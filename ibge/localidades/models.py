# coding: utf-8

from django.db import models

from django.contrib.localflavor.br import br_states

REGIOES = {
    '1': u'Norte',
    '2': u'Nordeste',
    '3': u'Sudeste',
    '4': u'Sul',
    '5': u'Centro-Oeste',
}

UFS = dict([(nome, sigla) for sigla, nome in br_states.STATE_CHOICES])

class Localidade(models.Model):
    cd_geocodi = models.CharField(db_index=True, max_length=20)
    tipo = models.CharField(db_index=True, max_length=10)
    cd_geocodb = models.CharField(db_index=True, max_length=20, blank=True)
    nm_bairro = models.CharField(db_index=True, max_length=60, blank=True)
    cd_geocods = models.CharField(db_index=True, max_length=20)
    nm_subdist = models.CharField(db_index=True, max_length=60, blank=True)
    cd_geocodd = models.CharField(db_index=True, max_length=20)
    nm_distrit = models.CharField(db_index=True, max_length=60)
    cd_geocodm = models.CharField(db_index=True, max_length=20)
    nm_municip = models.CharField(db_index=True, max_length=60, blank=True)
    nm_micro = models.CharField(db_index=True, max_length=100, blank=True)
    nm_meso = models.CharField(db_index=True, max_length=100, blank=True)
    nm_uf = models.CharField(db_index=True, max_length=60)
    cd_nivel = models.CharField(db_index=True, max_length=1)
    cd_categor = models.CharField(db_index=True, max_length=5)
    nm_categor = models.CharField(db_index=True, max_length=50)
    nm_localid = models.CharField(db_index=True, max_length=60)
    long = models.DecimalField(db_index=True, max_digits=24, decimal_places=6)
    lat = models.DecimalField(db_index=True, max_digits=24, decimal_places=6)
    alt = models.DecimalField(db_index=True, max_digits=24, decimal_places=5, null=True)

    def uf(self):
        return UFS[self.nm_uf]

    def regiao(self):
        meso = self.nm_meso.strip()
        micro = self.nm_micro.strip()
        if micro or meso:
            if micro == meso:
                res = meso + u'/='
            else:
                res = meso + u'/' + micro
        else:
            res = u''
        return res

