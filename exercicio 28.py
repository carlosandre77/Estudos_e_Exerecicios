"""o algoritimo sorteia um numero de 0 a 5
e peça para o usuario tentar descobrir qual foi o numero
escolhido pelo computado"""
import random
import playsound
n1=int(input('digite um numero de 0 a 5: '))
n2 = (random.randint(0,5))
while n1 > 5:
    print(n1,' é maior que 5')
    n1 = int(input('digite um numero de 0 a 5: '))
else:
    if n1==n2:
        playsound.playsound('acertou_mizeravi2.mp3')
        print('{} acertou mizeravi'.format(n2))
    else:
        print('{} errou!!'.format(n2))
        playsound.playsound('errou_faustao.mp3')