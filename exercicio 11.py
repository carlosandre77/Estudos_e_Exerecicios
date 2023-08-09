"""o algoritimo recebe a altura e largura de uma parede e calcula a quantidade de tinta nescessaria para pintala levando em consideração que cada litro pinta 2 m^2"""
altura = int(input('digite um altura : '))
largura =int(input('digite um largura : '))
area = largura*altura
quantidade = area/2
print('area é :{} é nescessario :{} litros de tinta para pintar'.format(area,quantidade))
 
