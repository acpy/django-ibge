from django.conf.urls import patterns, include, url

from .api import RegiaoResource, MesoRegiaoResource

regiao_resource = RegiaoResource()
meso_regiao_resource = MesoRegiaoResource()

urlpatterns = patterns('',
    url(r'^api/', include(meso_regiao_resource.urls)),
    url(r'^api2/', include(regiao_resource.urls)),
)
