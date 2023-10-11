# # metodos úteis dos dicionarios em Python
# len - quantas chaves
# keys - iteráveis com as chaves
# values - iteráveis com os valores
# itens - iteraveis com chaves e valores
# setdefealt - adiciona valor se a chave não existe
# copy - retorna uma copia rasa (SHADOW COPÝ)
# get - obtém uma chave
# pop - Apaga um item com chave especifica (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionario com outro


pessoa = {
    'nome': 'Carlos André',
    'sobrenome' : 'Carvalho',
    'sobrenome2' : 'silva',
    'sobrenome3': 'bernardinho',
#    'idade' : 30,
    'altura' : 1.8,
    }


# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))
# pessoa.setdefault('idade', None)
# print(pessoa['idade'])

import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0,1,2],  
}

d2 = copy.deepcopy(d1)
d2['l1'][1] = 1000

print(d1,d2)



# for chave,valor in pessoa.items():
#      print(chave,' - ',valor) 
