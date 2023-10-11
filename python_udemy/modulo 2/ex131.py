list_de_numeros_inteiros = [
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,3,7,8,5,10],
    [9,1,8,9,9,7,2,1,6,8],
    [1,3,2,2,8,6,5,9,6,7],

]
lista_indice = []
count = 0
for lista in list_de_numeros_inteiros:
    for i in lista:
        if i in lista_indice:               
            lista_indice.append(i)
            count += 1
            if count >= 2:
                lista_indice = []
                count = 0
                print(f'O valor duplicado da lista é {i}')
                break
                
        else:
           lista_indice.append(i)
    if len(lista_indice)  == len(lista):
        print('a lista não tem um segundo indice duplicado')
            
        