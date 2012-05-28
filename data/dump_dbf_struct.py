from dbf_rw import dbfreader
from pprint import pprint
from bz2 import BZ2File

ENCODING_DBF = 'cp1252'
arq_dbf = BZ2File('BR_Localidades_2010_v1.dbf.bz2')
localidades = dbfreader(arq_dbf)

nomes = []
tipos = []
for i, loc in enumerate(localidades):
    if i == 0:
        nomes = loc
    elif i == 1:
        tipos = loc
    else:
        break

pprint(zip(nomes, tipos))
