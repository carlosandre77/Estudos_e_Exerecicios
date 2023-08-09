"""faça um programa que leia o nome
completo de uma pessoa, mostrando em seguida
o primeiro e o último nome separadamente """
nome=str(input('digite digite o nome: ')).strip()
div= nome.split()
print('o primeiro  nome é: {}'.format(div[0]))
print('o ultimo  nome é: {}'.format(div[len(div)-1]))