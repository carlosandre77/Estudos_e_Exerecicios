
def mult(*args):
    resultado = 1
    for numero in args:
        resultado *= numero 
    return resultado

def par_ou_impar(resultado):
    mensagem = ''
    if resultado % 2 == 0:
        mensagem = 'o numero é par: '
    else: 
        mensagem = 'o numero é impar' 
    return  mensagem 


print(mult(5,6,6,4))
print(par_ou_impar(5)) 