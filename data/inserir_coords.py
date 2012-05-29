import json

munis = json.load(open('municipios.json'))
coords = json.load(open('coords.json'))

achados = 0
for muni in munis:
    codmuni = str(muni['pk'])
    cpos = muni['fields']
    rg_coord = coords.get(codmuni)
    if rg_coord:
        achados += 1
        uf, capital, geohash, lat, long, nome = rg_coord
        assert uf == cpos['uf']
        # XXX: falta resolver divergencias de nomes
        if cpos['nome'] != nome:
            #print cpos['nome'].ljust(30), nome
            cpos['nome'] = nome
        cpos['capital'] = bool(capital)
        cpos['geohash'] = geohash
        cpos['latitude'] = lat
        cpos['longitude'] = long
    else:
        cpos['capital'] = False
        cpos['geohash'] = ''
        cpos['latitude'] = None
        cpos['longitude'] = None

print achados, 'achados em', len(munis)

with open('muni_coords.json', 'wb') as saida:
    json.dump(munis, saida)
