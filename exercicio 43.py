"""desenvolva uma logica que leia o peso e a altura de uma pessoa.
calcule seu IMC emostre seu status, de acordo com a tabela abaixo
-abaixo da 18.5: abaixo do peso
-entre 18.5 e 25: peso ideal
-25 até 30: sobrepeso
-30 até 40:obesidade
-acima de 40: obesidade morbida"""
peso=(float(input('digite seu peso: ')))
altura=(float(input('digite sua altura: ')))
imc=peso/(altura*2)
if imc < 18.5 :
    print('seu IMC é {} voce esta abaixo do peso'.format(imc))
elif 18.5 <= imc < 25:
    print('seu IMC é {} voce esta no peso ideal'.format(imc))
elif 25  <= imc < 30:
    print('seu IMC é {} voce esta com sobrepeso'.format(imc))
elif 30  <= imc < 40:
    print('seu IMC é {} voce esta com obesidade'.format(imc))
elif imc > 40:
    print('\033[31mseu IMC é {} voce esta com obesidade morbida'.format(imc))

