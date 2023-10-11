"""faça um programa que leia um frase pelo teclado e mostre
1- quantas veses aparecem a letra 'a'
2- em que posição ela aparece a primeira vez
3- que posição ela aparece a ultima vez"""
frase=(input('digite um frase : ')).lower().strip()
print('1: ',frase.count('a'))
print('2: ',frase.find('a')+1)
print('3: ',frase.rfind('a')+1)


