from django.conf.urls import patterns, include, url

from .views import MunicipioListView, UFListView
from .views import RegiaoListView, MesoRegiaoListView

urlpatterns = patterns('',
    #url(r'^api/uf/([A-Za-z]{2})/', MunicipioPorUFListView.as_view()),
    url(r'^api/uf', UFListView.as_view()),
    url(r'^api/muni', MunicipioListView.as_view()),
    url(r'^api/regiao', RegiaoListView.as_view()),
    url(r'^api/mesoreg', MesoRegiaoListView.as_view()),
)
