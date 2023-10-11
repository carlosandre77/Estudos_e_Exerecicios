# exercicio - sistemas de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1','3','4','5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é  5*5',
        'Opções': ['25','55','10','51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é  10/2?',
        'Opções': ['4','5','2','1'],
        'Resposta': '5',
    },
]

escolha = 0
for pergunta in perguntas:
    print('pergunta: ', pergunta['Pergunta'])

    opcoes = pergunta['Opções']    
    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i+1})', opcao)
    
    escolha = input('Digite uma opção: ')
    
    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)
    

    while not escolha.isdigit() and int(escolha) > 0 and int(escolha) > qtd_opcoes:
        escolha = input('o valor digitado não é válido digite novamente: ')
    else:
        escolha_int = int(escolha)


    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int-1] == pergunta['Resposta']:
                acertou = True
       
    if acertou:
        print('acertou ✅ ')
    else:
        print('errou ❌')
    print()
    break


        # resposta_correta = pergunta['Opções'].index(1)
    # resposta = input()
    # if resposta == pergunta['Resposta']:
    #     print('Resposta correta')

  
  
    # resposta = input()

    