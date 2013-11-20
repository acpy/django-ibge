# coding: utf-8

import json

from .models import Municipio, MesoRegiao, REGIOES, UFS, REGIOES_UFS

from django import http
from django.views.generic.list import BaseListView

from django.forms.models import model_to_dict
from django.contrib.localflavor.br import br_states

class JSONResponseMixin(object):
    ''' Classe `mixin` baseada no exemplo em:
        https://docs.djangoproject.com/en/dev/topics/class-based-views/
    '''
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)

class JSONView(JSONResponseMixin, BaseListView):
    """Devolve a instância do model em formato JSON"""

class RegiaoListView(JSONView):
    queryset = [dict(id=id, nome=nome) for id, nome in REGIOES]

class UFListView(JSONView):
    def get_queryset(self):
        queryset = [dict(id=sigla, nome=nome)
                     for sigla, nome in br_states.STATE_CHOICES]
        if len(self.args) > 0:
            cod_reg = int(self.args[0])
            ufs_regiao = [uf for regiao, uf in REGIOES_UFS if regiao==cod_reg]
            queryset = [dic for dic in queryset if dic['id'] in ufs_regiao]
        return queryset

class MesoRegiaoListView(JSONView):
    def get_queryset(self):
        queryset = MesoRegiao.objects.all()
        if len(self.args) > 0:
            uf = self.args[0]
            queryset = queryset.filter(uf=uf)
        return [model_to_dict(mr) for mr in queryset]

class MunicipioListView(JSONView):
    def get_queryset(self):
        queryset = Municipio.objects.all()
        if 'meso' in self.kwargs:
            meso = self.kwargs['meso']
            queryset = queryset.filter(meso_regiao=meso)
        return [model_to_dict(mr) for mr in queryset]



