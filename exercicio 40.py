"""crie um programa que leia duas notas de um aluno e calcule sua media
mostrandouma mensagem no final.de acordo com amedia atingida
menor que 5.0 - reprovado
5.0 a 6.9     - recuperação
maior que 7.0 - aprovado"""
lista = []
nota = 0
notafinal=0
cont=0
while nota != -1:
    print('\033[33m digite -1 para finalizar\033[m')
    lista.append(cont)
    nota= float(input('digite sua  nota: '))
    notafinal=nota+notafinal
    cont = cont + 1
if nota == -1:
    cont=cont-1
    notafinal= notafinal+1
if (notafinal/cont)<5:
    print('sua media é: ',(notafinal/cont))
    print('você é burro')
elif (notafinal/cont) > 5 and (notafinal/cont)< 7:
    print('sua media é: ',(notafinal/cont))
    print ('recuperação')
else:
    print('sua media é: ',(notafinal/cont))
    print('voce passou')
print(cont)
print(notafinal)
