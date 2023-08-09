"""faça um programa que leia um angulo qualquer e
mostre na tela o valor do seno, cosseno e tangente"""
import math
angulo= (float(input('digite o angulo : ')))
seno=math.sin(math.radians(angulo))
coseno=math.cos(math.radians(angulo))
print('o seno de {} é {} e o coseno é {:.2f} '.format(angulo,seno,coseno))