from django.conf.urls import patterns, include, url

from .views import RegiaoListView, MunicipioListView, MesoRegiaoListView

urlpatterns = patterns('',
    url(r'^api/muni', MunicipioListView.as_view()),
    url(r'^api/regiao', RegiaoListView.as_view()),
    url(r'^api/mesoreg', MesoRegiaoListView.as_view()),
)
