"""
args - Argumentos não nomeados 
*- *args (empacotamento e desenpacotamento)
"""

# Lembre-te de desempacotamento
#x, y, *resto =1,2,3,4
#nprint(x,y,resto)

# def soma(x,y):
#   return x+ y

#x, y, *resto = 1,2,3,4
#print(z,y, resto)

def soma(*args):
    total = 0
    for numero in  args:
        total += numero
    return total 


numeros = 1,2,3,4,5,50,51,800
soma1 = soma(*numeros,10)
print(soma1)