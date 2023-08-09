"""um professor quer sortear um dos seus quatro alunos para apagar
 o quadro. faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido"""
from random import choice
n1=str(input('primeiroaluno: '))
n2=str(input('segundo aluno: '))
n3=str(input('terceiro aluno: '))
n4=str(input('quarto aluno: '))
lista=(n1,n2,n3,n4)
print('o aluno escolhido foi: {}' .format(random.choice(lista)))