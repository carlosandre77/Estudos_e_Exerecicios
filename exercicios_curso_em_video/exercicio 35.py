"""desenvolva um programa que leia o comprimento
de tres retas e diga ao usuario se elas podem ou
nãp formar um triangulo"""
print('-='*20)
print(('analizador de triangulos'.center(40)))
print('-='*20)
r1=(int(input('digite a primeira reta : ')))
r2=(int(input('digite a segunda  reta : ')))
r3=(int(input('digite a terceira reta : ')))
if (r1+r2)>r3 and (r1+r3)>r2 and (r3+r2)>r1:
    print('as retas formam um triangulo ')
else:
    print('não é um triangulo:')
