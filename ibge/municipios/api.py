from tastypie.resources import Resource, ModelResource
from tastypie import fields
from .models import MesoRegiao, REGIOES

class Regiao(object):
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def to_dict(self):
        return self.__dict__

regioes = [Regiao(id_reg, nome) for id_reg, nome in REGIOES]

class RegiaoResource(Resource):
    id = fields.CharField(attribute='id')
    nome = fields.CharField(attribute='nome')

    class Meta:
        object_class = Regiao
        resource_name = 'regiao'

    def get_resource_uri(self, bundle_or_obj):
        kwargs = {'resource_name': self._meta.resource_name}
        return self._build_reverse_url("api_dispatch_detail", kwargs=kwargs)

    def get_object_list(self, request):
        return regioes.values()

    def obj_get_list(self, request=None, **kwargs):
        # Filtering disabled for brevity...
        return self.get_object_list(request)

    def obj_get(self, request=None, **kwargs):
        return regioes[int(kwargs['pk'])-1]

class MesoRegiaoResource(ModelResource):
    class Meta:
        queryset = MesoRegiao.objects.all()
        resource_name = 'mesoregiao'
