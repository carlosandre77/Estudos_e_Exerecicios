"""jokenpo"""

from random import randint
from time import sleep
opcao=(int(input('''qual sua jogada :
[0] pedra
[1] papel
[2] tesoura
''')))
itens=('pedra','papel','tesouta')
cpu = randint(0,2)
print('JO')
sleep(0.5)
print('KEN')
sleep(1)
print('PO!!!!')
sleep(1)
print('-='*20)
print('O computador jogou: ',itens[cpu])
print('voce jogou: ',itens[opcao])
print('-='*20)

if cpu == 0 and opcao == 0 or cpu == 1 and opcao == 1 or cpu == 2 and opcao == 2:
    print('empate')
elif cpu == 0 and opcao == 1 :
    print('você ganhou')
elif cpu == 0 and opcao == 2 :
    print('você perdeu')
elif cpu == 1 and opcao == 0 :
    print('você perdeu')
elif cpu == 1 and opcao == 2 :
    print('você ganhou')
elif cpu == 2 and opcao == 0 :
    print('você ganhou')
elif cpu == 2 and opcao == 1 :
    print('você perdeu')