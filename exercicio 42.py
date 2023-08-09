"""crie um programa que leias os lados de um triangulo e diaga se ele é isóceles escaleno equilatero"""
reset=0
while reset!=-1:
    print('-='*20)
    print(('analizador de triangulos'.center(40)))
    print('-='*20)
    r1=(int(input('digite a primeira reta : ')))
    r2=(int(input('digite a segunda  reta : ')))
    r3=(int(input('digite a terceira reta : ')))
    if (r1+r2)<r3 or (r1+r3)<r2 or (r3+r2)<r1:
      print('não é um triangulo:')
    elif r1!=r2 != r3 != r1:
        print('é um triangulo escaleno ')
    elif r1==r2 and r1==r3:
        print('é um triangulo equilatero ')
    elif r1==r2 and r1!=r3 or r1==r3 and r1!=r2:
        print('é um triangulo isoceles ')
    print('-=' * 20)
    reset =(int(input('digite -1 para finaliza 0 para recomeçar: ')))
