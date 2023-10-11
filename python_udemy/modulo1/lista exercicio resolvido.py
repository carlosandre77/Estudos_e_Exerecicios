import os
lista = []

while True:
    print('Selecione uma opção:')
    opcao = input('[i]inserir [a]apagar [l]listar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
        
    elif opcao == 'a':
        indice_srt = input(
        'Escolha o indice para apagar: '
        )

        try:
            indice = int(indice_srt)
            del lista[indice]
        except ValueError:
            print('Digite um numero inteiro')
        except IndexError:
            print('Indice não existe!')
    elif opcao =='l':
        os.system('cls')

        if len(lista) ==0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Porfavor, escolha i, a ou l. ')
    
