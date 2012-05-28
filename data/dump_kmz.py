# coding: utf-8
import zipfile

from xml.etree import ElementTree

import re

ARQ = 'cidades_do_brasil_2008.kmz'


NOMES_ERRADOS = {
    u'AceguáV':(u'Aceguá', 'RS'),
    u'Antônio Prado de Minas':(u'Antônio Prado de Minas', 'MG'),
    u'Campo MaiorV':(u'Campo Maior', 'PI'),
    u'CanavieiraV':(u'Canavieira', 'PI'),
    u'Itaguaí':(u'Itaguaí', 'RJ'),
    u"Pau d'Arco":(u"Pau d'Arco", 'TO'),
    u'São Domingos de Pombal':(u'São Domingos de Pombal', 'PB'),
}

def extrair_nome_uf(ns, elem):
    nome = elem.findtext(ns+'name')
    assert nome is not None, 'elemento <name> nao encontrado'
    if '/' in nome:
        nome, uf = nome.split('/')
    elif nome in NOMES_ERRADOS:
        nome, uf = NOMES_ERRADOS[nome]
    else:
        raise NameError('nome desconhecido: %r' % nome)
    return nome, uf

RE_CODMUN = re.compile(r'infomun\.asp\?codmun=(\d{7})')

def extrair_codmun(ns, elem):
    descr = elem.findtext(ns+'description')
    assert descr is not None, 'elemento <description> nao encontrado'
    codmun = RE_CODMUN.search(descr)
    assert codmun is not None, u'regex codmun nao bateu:'+descr
    return codmun.group(1)

def extrair_coords(ns, elem):
    point = elem.find(ns+'Point')
    coords = point.findtext(ns+'coordinates')
    assert coords is not None, 'elemento <coordinates> nao encontrado'
    if ',' in coords:
        long, lat, _ = [float(n) for n in coords.split(',')]
    else:
        raise ValueError('coordenadas mal formadas: %r' % coords)
    return lat, long

with zipfile.ZipFile(ARQ) as kmz:
    doc = kmz.open('doc.kml')
    raiz = None
    qt_lidos = 0
    for event, elem in ElementTree.iterparse(doc):
        ns = elem.tag[:elem.tag.find('}')+1]
        if elem.tag == ns+'Placemark':
            nome, uf = extrair_nome_uf(ns, elem)
            codmun = extrair_codmun(ns, elem)
            lat, long = extrair_coords(ns, elem)
            qt_lidos += 1
            print qt_lidos, uf, codmun, lat, long, nome
            #break


'''
  context = iterparse(source, events=("start", "end"))
  root = None

  for event, elem in context:
      if event == "start" and root is None:
          root = elem     # the first element is root
      if event == "end" and elem.tag == "record":
          ... process record elements ...
          root.clear()

'''
