# sets - Conjubntos em Python ( tipo set)
# Conjunto são ensinados na matematica
# Representados graficamente pelo diagrama de venn
# Sets em Python são mutáveis, porem aceitam apenas
# tipos imutáveis como valor inteiro.

#criando um set
# set(iterável)

# s1 = set('Luiz')
# s1 = set() #vazio
# s1 = {'Luiz',1,2,3} #com dados


# Sets são eficientes para remover valores duplicados de iteraveis 
# - eles não tem índexes;
# - eles não garantem ordem
# - eles são iteráveis (for, in, not in)
# s1 = {1,2,3,3,3,3,3}
# print(s1)

# métodos úteis:
# add, update, clear, dicard

s1 = set()
s1.add('Luiz')
s1.add(1)
s1.update(('Olá mundo',1,2,3,4,4))
# s1.clean
s1.discard('Olá mundo')
s1.discard('Luiz')
# print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos 
# s1 = {1,2,3}
# s2 = {2,3,4}
# s3 = s1 | s2
# s3 = s1 & s2
# s3 = s1 - s2
# s3 = s1 ^ s2
# print(s3)

letras =  set()
while True:
    letra = input('Digite: ')
    letras.add(letra)

    if 'l' in letras:
        print('PARABÈNS')
        break

    print(letras)
