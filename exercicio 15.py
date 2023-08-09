"""escreva  um programa que pergunte a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. calcule o preço a pagar, sabendo que
 o carro custa 60$ por dia e 0.15 por km rodaado"""

km= int(input('digite a quantidade de km rodados: '))
dias= float(input('digite a quantidade de dias  alugados: '))
print('o valor por km andados é {:.2f} /e o valor pelos dias de alugiel é {:.2f} '.format((km*0.15),(dias*60)))
