"""imprecisão de ponto flutuante
Double-precision floatng-point format 754"""

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_2 + numero_1
print(numero_3)
print(f'{numero_3:.3f}')
print(round(numero_3,3))