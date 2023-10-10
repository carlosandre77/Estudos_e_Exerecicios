"""crie um programa que leia o nome completo de um pessoa e mostre
1-o nome com todas as letras
2- o nome com todas minusculas
3- quantas letras(sem considerar espaços
4- quantas letras tem o primeiro nome"""
nome=input('digite seu nome completo: ')
dividir= (nome.split())
print('1: ', nome.title())
print('2: ', nome.lower())
print('3: ', len(nome))
print('4: ', len(dividir[1]))
