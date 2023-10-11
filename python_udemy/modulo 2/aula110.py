"""
Retorno de valores das funções(return)
"""
def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma(1,2,3,4,5,6)