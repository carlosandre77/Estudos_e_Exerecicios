"""faca um programa que leia um ano qualquer e mostre se ele é bisexto"""
from datetime import date
ano=(int(input('digite o ano (para data atual "0" para finalizar "-1": ')))
while ano != -1 :
    while ano < -1 or ano > 9999 :
        print('{} ano invalido'.format(ano))
        ano=(int(input('digite um ano valido: ')))
    else:
        if ano == 0:
            ano = date.today().year
        else:
            if ano % 4 == 0 and ano % 100 != 0 or ano % 400== 0:
                print("o ano {} é bisexto".format(ano))
                ano = (int(input('digite o ano (para data atual "0" para finalizar "-1": ')))
            else:
                print("o ano {} não é bisexto".format(ano))
                ano = (int(input('digite o ano (para data atual "0" para finalizar "-1": ')))
