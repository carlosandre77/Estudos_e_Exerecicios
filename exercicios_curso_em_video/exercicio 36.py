"""escreva um programa para aprovar o emprestimo bancario para compra
de uma casa. o programa vai perguntar o valor da casa, o salario do comprador
e em quantos anos ele vai pagar.
calcule o valor da prestação mensal , sabendo que ela não pode exercer 30% do salario
ou então o emprestimo será negado"""
valor_da_casa=float(input('digite o valor da casa: '))
salario=float(input('digite o valor do salario: '))
ano=float(input('digite quantos anos para pagar: '))
prestacao = valor_da_casa/(ano*12)
if prestacao < (salario*30/100):
    print('o vaor da prestação será: ',prestacao)
elif prestacao > (salario*30/100):
    print('você é pobre')
