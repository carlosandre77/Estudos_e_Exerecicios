"""faça um programa que leia um numero de
0 9999 e mostre na tela caum dos digitops separados"""
numero= int(input('digite um numero de 0 a 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('unidade: ',(u))
print('dezena: ',(d))
print('centena: ',(c))
print('milhar: ',(m))