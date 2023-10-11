list_de_numeros_inteiros = [
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,3,7,8,5,10],
    [9,1,8,9,9,7,2,1,6,8],
    [1,3,2,2,8,6,5,9,6,7],
]

def encontra_primeiro_duplicado(lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1
    for numero in lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero) 

    return primeiro_duplicado

for lista in list_de_numeros_inteiros:
    print(
        lista,
        encontra_primeiro_duplicado(lista)
    )