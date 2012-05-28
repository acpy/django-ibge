
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




