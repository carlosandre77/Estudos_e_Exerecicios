"""crie um programa que leia uma frase qualquer e diga se ela é um palindromo"""
frase=str(input('digite a frase: ')).strip().upper()
palavras=frase.split()
junto="".join(palavras)
if junto == junto[::-1]:
    print('a frase é um palindromo ')
else:
    print('a frase não éum palindromo ')