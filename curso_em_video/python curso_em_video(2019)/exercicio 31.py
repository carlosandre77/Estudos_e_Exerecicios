"""desenvolva  um programa que pergunte a distancia de uma viagem
em km. calcule o preço da passagem, cobrado r$ 0,50 por km para viagens de até
200Km e r$0,45 par aviagens mais longas"""
n1=float(input('digite a distancia que será percorrida: ' ))
if n1 > 200 :
    print('o custo da viagem é: ',n1*0.45)
else:
    print('o custo da viagem é: ',n1*0.50)