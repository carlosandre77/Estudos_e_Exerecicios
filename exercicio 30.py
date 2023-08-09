"""crie um programa que leia um numero inteiro e mostre se ele é par ou impar"""
n1= int(input('digite um numero: '))
if n1 % 2 == 0:
    print('o numero {} é par '.format(n1))
else :
    print(' o numero {} é impar '.format(n1))