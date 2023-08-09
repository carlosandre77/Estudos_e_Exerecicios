"""escreva um programa que leia um numero inteiro qualquer e peça
 para o usuario escolher qual a base de converção
 1-  para binario
 2- para octal
 3- para hexadecimal"""
n1=int(input('digite um numero: ' ))
i=[]
cont=0
while n1 >= 1:
    i=n1 % 2
    n1= n1//2
    cont=cont+1
    print(i[0])