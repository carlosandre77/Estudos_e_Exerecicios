"""elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
-à cista dinheiro/cheque:10% de desconto         - em até 2x no cartão: preço normal
-à vista no cartão : 5% de desconto              - 3x ou mais no cartão:20% de juros"""
preco=(float(input('digite o valor do produto: ')))
cond=(float(input('''como deseja pagar?:
1 - à vista dinheiro/cheque:10% de desconto / 2 - à vista no cartão : 5% de desconto / 3 - a prazo 
''')))
parcelas=1
if cond == 1 :
    opcao = preco - (preco * 10 / 100)
elif cond == 2:
    opcao= preco-(preco *5/100)
elif cond == 3:
    parcelas=(int(input('''digite a quantidade de parcelas :
- em até 2x no cartão: preço normal    - 3x ou mais no cartão:20% de juros
''')))
    if  parcelas > 1 and parcelas <= 2:
        opcao = (preco/parcelas)
    elif  parcelas > 2 and parcelas <= 38:
        opcao = (preco-(preco*20/100))
print('o valor a pagar é {}x de {} '.format(parcelas,opcao))