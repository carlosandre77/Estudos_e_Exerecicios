"""esccreva um priograma que pergunte o salario de um fucionario e
calcule o valor do seu aumento.
para salarios superiores a r$ 1.250,00 calcule um almento de 10$
para os inferiores ou iguais, o aumento é de 15%"""
salario=float(input('digite o salario: '))
if salario > 1250:
    salario= salario+(salario * 15/100)
else:
    salario= salario+(salario * 10/100)
print('o valor do salario com o almento é {} :'.format(salario))
