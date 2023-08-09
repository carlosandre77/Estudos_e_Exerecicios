"""escreva um programa que leia doisnumeros inteiros e compare-os.
mostrando na tela uma menssagem"""
n1=int(input('digite um numero: ' ))
n2=int(input('digite outro numero' ))
n3=int(input('digite outro numero' ))

if n1 == n2 and n1==n3 :
    print('os valores são iguais')
elif n1> n2 and n1> n3:
    print('{} é maior : '.format(n1))
elif n2> n1 and n2> n3:
    print('{} é maior : '.format(n2))
elif n3 > n2 and n3 > n1:
    print('{} é maior : '.format(n3))

