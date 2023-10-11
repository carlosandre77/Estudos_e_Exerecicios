# List comprehension em Pythom
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis
 
#print(list(range(100)))
import pprint

def p(v):
    pprint.pprint(v, sort_dicts = False, width=40)


lista = []
for numero in range(10):
    lista.append(numero)

lista = [
    numero * 2
    for numero in range(10)
]
# print(lista)

# Mapeamento de dados em list comprehension
produtos  = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] *1.05 }
    for produto in produtos
]

# print(novos_produtos)
# print(*novos_produtos, sep='\n')
# p(novos_produtos)
# lista = [n for n in range(10) if n < 5]

novos_produtos = [
    {**produto, 'preco': produto['preco'] *1.05 }
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05)> 1
]
p(novos_produtos)