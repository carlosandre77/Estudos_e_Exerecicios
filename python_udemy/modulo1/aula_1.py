"""
Faça uma lista de compras
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista_compras = ['João','Maria','José','miguel']
inicio = ''

while inicio != 'S':    

    inicio = ''
    while inicio != 'S' and\
        inicio !='I' and inicio != 'EU' and\
        inicio != 'EI':
        inicio = input('Para Sair digite "S" '
        'Incluir item na lista digite "I" '
        'Excluir ultimo item digite "EU" ' 
        'Excluir por indice digite "EI": ').upper()
        
        if inicio == 'I':
            lista_compras.append(input('Digite o itens da lista: '))

        if inicio == 'EU':
            lista_compras.pop()
        if inicio == 'EI':
            
            for indice,item in enumerate(lista_compras):
                print(indice,item)
            indice_p_excluir = input('digite o indice para excluir: ' )
            

            try:
                del(lista_compras[int(indice_p_excluir)])
            
            except IndexError:
                print('fora do range')

        print(f'Suas compras são:\n {lista_compras}')

    else:
        continue

else:
    print(f'{5*"#"} fim algoritimo {5*"#"}')



