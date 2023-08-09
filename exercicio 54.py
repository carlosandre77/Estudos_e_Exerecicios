"""crie um programa que leia o ano de nascimento
de sete pessoas. no final, mostre quantas pessoas ainda
não atingiram amaior idade e quantas ja são maiores."""
from datetime import date
atual= date.today().year
maior=0
menor=0
for c in range(1,8
               ):
    ano = int(input('digite o ano de nascimento da {}° pessoa : '.format(c)))
    if  (atual-ano) <= 18:
        menor+=1
    else:
        maior+=1

print(maior)
print(menor)