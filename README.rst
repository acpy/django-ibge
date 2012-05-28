
========================
Códigos de Áreas do IBGE
========================

Conforme a página oficial do IBGE_:

  A Tabela de Códigos de Municípios, elaborada pelo IBGE, apresenta a lista
  dos municípios brasileiros associados a um código composto de 7 dígitos,
  sendo os dois primeiros referentes ao código do estado.

.. _IBGE: http://www.ibge.gov.br/concla/cod_area/cod_area.php

Na prática, os dados encontrados em formato .DBF contém mais do que os
municípios, mas também distritos, subdistritos, bairros e setores, em
uma hierarquia de códigos de 7 a 15 dígitos, respectivamente.

Fonte dos dados:

ftp://geoftp.ibge.gov.br/organizacao_territorial/localidades/Shapefile_SHP/BR_Localidades_2010_v1.dbf

Mais arquivos de dados do IBGE podem ser encontrados em:

ftp://geoftp.ibge.gov.br/

Descrição dos Campos
====================

Descrição dos Campos Finais para Features Geomedia, Shape e KML de Pontos de
Localidades 2010 em 28/11/2011.

Tabela convertida da Planilha .XLS encontrada em:
ftp://geoftp.ibge.gov.br/organizacao_territorial/localidades/descritivo_campos_localidades_2010.xls

== ============== ========== ========== ====== =================================================================
#  Geomedia e KML Shape      Tipo       Tam.   Descrição
== ============== ========== ========== ====== =================================================================
1  ID             ID         Autonumber -      Contagem automárica de geometrias ponto oriundas de setor
2  CD_GEOCODIGO   CD_GEOCODI Text       20     Geocódigo do setor (15 dígitos numéricos)
3  TIPO           TIPO       Text       10     Classificação de Tipo (Urbano ou Rural, 6 dígitos alfa-numéricos)
4  CD_GEOCODBA    CD_GEOCODB Text       20     Geocódigo do bairro (12 dígitos numéricos)
5  NM_BAIRRO      NM_BAIRRO  Text       60     Nome do bairro
6  CD_GEOCODSD    CD_GEOCODS Text       20     Geocódigo do subdistrito (11 dígitos numéricos)
7  NM_SUBDISTRITO NM_SUBDIST Text       60     Nome do subdistrito
8  CD_GEOCODDS    CD_GEOCODD Text       20     Geocódigo do distrito (9 dígitos numéricos)
9  NM_DISTRITO    NM_DISTRIT Text       60     Nome do distrito
10 CD_GEOCODMU    CD_GEOCODM Text       20     Geocódigo do Município (7 dígitos numéricos)
11 NM_MUNICIPIO   NM_MUNICIP Text       60     Nome do Município
12 NM_MICRO       NM_MICRO   Text       100    Nome Micro-região
13 NM_MESO        NM_MESO    Text       100    Nome Meso-região
14 NM_UF          NM_UF      Text       60     Nome da UF
15 CD_NIVEL       CD_NIVEL   Text       1      Código do Nível da Localidade
16 CD_CATEGORIA   CD_CATEGOR Text       5      Código da Categoria da Localidade
17 NM_CATEGORIA   NM_CATEGOR Text       50     Nome da Categoria da Localidade
18 NM_LOCALIDADE  NM_LOCALID Text       60     Nome da Localidade
19 LONG           LONG       Double     6 dec. Longitude da Localidade em grau decimal
20 LAT            LAT        Double     6 dec. Latitude da Localidade em grau decimal
21 ALT            ALT        Double     2 dec. Altitude da Localidade, oriunda de SRTM em metros
== ============== ========== ========== ====== =================================================================

Análise dos dados
=================

========== =============== =============== ==== ==== ===== ==================================================================
nome campo       valor min       valor max zero null blank [curto] mais_longo
========== =============== =============== ==== ==== ===== ==================================================================
id                       2           21886  -    -     -   [-]
cd_geocodi 110001515000001 530010805200123  -    -     -   [110001515000001] 110001515000001
tipo       RURAL           URBANO           -    -     -   [RURAL] URBANO
cd_geocodb                 521830005002     -    -     B   [] 110004905003
nm_bairro                  progresso        -    -     B   [] Zona de Adensamento Controlado (ZAC - São Silvestre)
cd_geocods 11000151500     53001080520      -    -     -   [11000151500] 11000151500
nm_subdist                 ÁREA DE PLANEJA  -    -     B   [] QUARTA REGIÃO ADMINISTRATIVA (PRAIA DE CARAPEBUS)
cd_geocodd 110001515       530010805        -    -     -   [110001515] 110001515
nm_distrit ABADIA          ÓLEO             -    -     -   [BAÚ] NÚCLEO COLONIAL PIO XII (SÃO GERÔNIMO)
cd_geocodm 1100015         5300108          -    -     -   [1100015] 1100015
nm_municip                 ÓLEO             -    -     B   [] VILA BELA DA SANTÍSSIMA TRINDADE
nm_micro                   ÓBIDOS           -    -     B   [] SERGIPANA DO SERTÃO DO SÃO FRANCISCO
nm_meso                    ZONA DA MATA     -    -     B   [] CENTRO NORTE DE MATO GROSSO DO SUL
nm_uf      ACRE            TOCANTINS        -    -     -   [ACRE] RIO GRANDE DO NORTE
cd_nivel   1               6                -    -     -   [2] 2
cd_categor 00001           85               -    -     -   [15] 00001
nm_categor ALDEIA INDÍGENA VILA             -    -     -   [AUI] PROJETO DE ASSENTAMENTO
nm_localid 1               ÓRFÃO            -    -     -   [4] JARDIM CACHOEIRA CHÁCARA CLIMÁTICA BOCAINA PLANALTO DA SERRA
long        -73.4976133364  -32.4351863281  -    -     -   [-]
lat         -33.7375398486   5.22007072643  -    -     -   [-]
alt                    0.0     1639.154504  0    N     -   [-]
gmrotation             0.0             0.0  0    -     -   [-]
========== =============== =============== ==== ==== ===== ==================================================================

========
API REST
========

Um teste com a biblioteca Tastypie gerou as seguintes URLs para acesso REST
ao model cidades.models.MesoRegiao::

    ^muni/ ^api/ ^(?P<resource_name>mesoregiao)/$ [name='api_dispatch_list']
    ^muni/ ^api/ ^(?P<resource_name>mesoregiao)/schema/$ [name='api_get_schema']
    ^muni/ ^api/ ^(?P<resource_name>mesoregiao)/set/(?P<pk_list>\w[\w/;-]*)/$ [name='api_get_multiple']
    ^muni/ ^api/ ^(?P<resource_name>mesoregiao)/(?P<pk>\w[\w/-]*)/$ [name='api_dispatch_detail']

Acessando a primeira URL com parâmetros::

  http://localhost:8000/muni/api/mesoregiao/?limit=3&format=json

Resultado::

    {"meta": {"limit": 3, "next": "/muni/api/mesoregiao/?offset=3&limit=3&format=json",
              "offset": 0, "previous": null, "total_count": 137},
     "objects": [
       {"id": "21", "nome": "Agreste Alagoano", "nome_ascii": "Agreste Alagoano",
        "regiao": 2, "resource_uri": "/muni/api/mesoregiao/21/", "uf": "AL"},
       {"id": "43", "nome": "Agreste Paraibano", "nome_ascii": "Agreste Paraibano",
        "regiao": 2, "resource_uri": "/muni/api/mesoregiao/43/", "uf": "PB"},
       {"id": "47", "nome": "Agreste Pernambucano", "nome_ascii": "Agreste Pernambucano",
        "regiao": 2, "resource_uri": "/muni/api/mesoregiao/47/", "uf": "PE"}
    ]}

URL de detalhe::

  http://localhost:8000/muni/api/mesoregiao/11/?format=json

Resultado::

  {"id": "11", "nome": "Metropolitana de Bel\u00e9m", "nome_ascii": "Metropolitana de Belem",
  "regiao": 1, "resource_uri": "/muni/api/mesoregiao/11/", "uf": "PA"}


URL de conjunto::

  http://localhost:8000/muni/api/mesoregiao/set/11;15/?format=json

Resultado::

    {"objects": [
      {"id": "11", "nome": "Metropolitana de Bel\u00e9m", "nome_ascii": "Metropolitana de Belem",
       "regiao": 1, "resource_uri": "/muni/api/mesoregiao/11/", "uf": "PA"},
      {"id": "15", "nome": "Leste Rondoniense", "nome_ascii": "Leste Rondoniense",
       "regiao": 1, "resource_uri": "/muni/api/mesoregiao/15/", "uf": "RO"}
    ]}

URL do esquema da API e dados::

http://localhost:8000/muni/api/mesoregiao/schema/?format=json

Resultado::

    {"allowed_detail_http_methods": ["get", "post", "put", "delete", "patch"],
     "allowed_list_http_methods": ["get", "post", "put", "delete", "patch"],
     "default_format": "application/json",
     "default_limit": 20,
     "fields": {
       "id": {"blank": false, "default": "", "help_text": "Unicode string...",
              "nullable": false, "readonly": false, "type": "string", "unique": true},
       "nome": {"blank": false, "default": "No default provided.", "help_text": "Uni..",
              "nullable": false, "readonly": false, "type": "string", "unique": false},
       "nome_ascii": {"blank": false, "default": "No default provided.", "help_text": "Uni...",
              "nullable": false, "readonly": false, "type": "string", "unique": false},
       "regiao": {"blank": false, "default": "No default provided.",
              "help_text": "Integer data. Ex: 2673", "nullable": false, "readonly": false, "type": "integer", "unique": false},
       "resource_uri": {"blank": false, "default": "No default provided.", "help_text": "Uni...",
              "nullable": false, "readonly": true, "type": "string", "unique": false},
       "uf": {"blank": false, "default": "No default provided.", "help_text": "Uni..",
             "nullable": false, "readonly": false, "type": "string", "unique": false}
     }
    }

=============
Geohash
=============

Experimentei as bibliotecas `python-geohash`_ , bem documentada
e empacotada, e a `Geohash 1.0rc1`_, referenciada pela primeira.

.. _python-geohash: http://code.google.com/p/python-geohash/

.. _Geohash 1.0rc1: http://pypi.python.org/pypi/Geohash/

Fiquei com a Geohash, por ser escrita em Python puro, facilitando a
instalação em hosts compartilhados e na nuvem.
