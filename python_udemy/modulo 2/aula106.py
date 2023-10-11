"""
Argumentos nomeados e não nomeados em funções  Python
Argumento nomeado tem nome com sinal de igual
Argumentos não nomeado recebe apenas o argumento (valor)
"""
def soma(x,y, z=None):
    if z is not None:
            print(f'{x=} {y=} {z=} ',x+y+z)
    else:
        print(f'{x=} {y=}',x+y)
    

soma(5,15)
soma(3, 5)
soma(4,5,3)
