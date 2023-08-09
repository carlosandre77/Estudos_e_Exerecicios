"""faça um programa que três números e mostre qual éo maior e qual é o menor"""
n1=(float(input('digite primeiro numero: ')))
n2=(float(input('digite segundo numero: ')))
n3=(float(input('digite terceiro numero: ')))
if n1 == n2 and n1 == n2:
    print('iguais')
else:
#verificar menor
    menor = n1
    if n2 < n1 and n2<n3:
      menor=n2
    if n3 < n1 and n3<n2:
        menor=n3
    #verificar maior
    maior=n1
    if n2 > n1 and n2>n3:
        maior=n2
    if n3 > n1 and n3>n2:
        maior=n3
    print('o maior valor é {} e o menor é {}'.format(maior,menor))

