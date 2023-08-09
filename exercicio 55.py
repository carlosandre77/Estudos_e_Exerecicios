"""faça um programa que leia o peso de cinco pessoas. emostro qual foi o maior e o menor peso """

for c in range(1,6):
    peso=(float(input(' digite o {}° primeiro peso: '.format(c))))
    if c==1:
        maior=peso
        menor=peso
    else:
        if peso > maior:
           maior=peso
        if peso < menor:
           menor=peso
print('o maior peso é:{} kg '.format(maior))
print('o menor peso é:{} kg '.format(menor))