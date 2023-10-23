def calcular_distancia(localizacao1, localizacao2):
    lat1, lon1 = localizacao1
    lat2, lon2 = localizacao2
    distancia = ((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2) ** 0.5
    return distancia