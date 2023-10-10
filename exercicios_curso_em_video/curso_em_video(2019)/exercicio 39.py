"""faça um priograma que leia o ano de nascimento de um jovem e informe, de acordo com sua
idade, se ele ainda vai se alistar ao serviço militar,
se é a hora dese alistar ou se já passou do tempo de alistamento.
seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo"""
from datetime import date
ano=(int(input('digite o ano de anascimento: ')))
data=(date.today().year)
idade= data - ano
if idade < 18:
    print('\033[32m voce tem {} anos faltam {} anos para se alistar:  '.format(idade,(18-idade)))
elif idade > 18:
    print('\033[31m voce tem {} anos ja passou {} anos do ano de se alistar:  '.format(idade,(idade-18)))
elif idade == 18:
    print('\033[33m voce tem {} anos deve se alistar este ano:  '.format(idade))
