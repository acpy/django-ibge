
from .models import Municipio, MesoRegiao, REGIOES, UFS

from django import http
from django.views.generic.list import ListView

class HomeListView(ListView):
    queryset = [dict(id=id, nome=nome) for id, nome in REGIOES]
    template_name='municipios/home.html'
