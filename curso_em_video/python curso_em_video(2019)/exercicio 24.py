"""crie um programa que leia o nome de uma cidade e diga se ela começa 
ou não com "santo" """
nome = input('digite o nome da cidade: ')
div= nome.split()
print('santo' in div[0].lower())