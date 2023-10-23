def calcular_taxa_entrega(distancia):
    if distancia < 2.9:
        return 0
    elif 3 <= distancia <= 5:
        return 5
    elif 5.1 <= distancia <= 12:
        return 7
    else:
        return 12