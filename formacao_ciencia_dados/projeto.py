# importar bibllioteca 'math'com a fução sqrt(raiz quadrada)
# importar o arquivo com as funçoes de carregar e exportar dados
from math import sqrt
from manipulate_data import load_json_file, save_json_file

# definindo as variaveis
restaurante = []
sair = 'S' 
cont = 0 
loc = [2,2] # localização do fornecedor para ser usada para caucular as distancias

# definindo os cardapios
tradicional = ['hamburguer','batata frita']
vegano = ['salada','aveia']
cardapios = [tradicional,vegano]

# dados_carregados = load_json_file('export','arquivo')
# lista_ids = []
# for i in dados_carregados:
#     lista_ids.append(i[0])

# maior_id = max(lista_ids)
# cont = maior_id[0] 
# print(cont)


#dentro do loop ficara todo o codigo ao final de cada laço as informações do restalrante será salva no arquivo.json
while True:
    sair = input('Deseja cadastrar restaurante?(S/N): ').upper()

    if sair == 'N':
        break

    # A função load_json_file carrega os dados do arquivo salvo, depois salva na variavel dados_carregados 
    dados_carregados = load_json_file('export','arquivo')
    lista_ids = []

    for i in dados_carregados:
        lista_ids.append(i[0])
    
    maior_id = max(lista_ids) 
    
    
    restaurante.append([[maior_id[0]+1]]) # usa o valor do contador para criar o codigo do id
    restaurante[cont].append(input('Digite o nome do restaurante: ')) 
    
    # recebe uma string dividindo em 2 valores usando a ',' como separador Ex: '3,4' -> ['3','4'] 
    restaurante[cont].append(input('Digite as coordenadas do restaurante Ex(latitude,longitude): ').split(','))

    lat = float(restaurante[cont][2][0])
    long = float(restaurante[cont][2][1])
    
    # cauculo da distancia euclidiana raiz((x1 - x2)^2 + (y1 - y2)^2) 
    distancia = sqrt(( loc[0] - lat )** 2 + (loc[1] - long )**2 )
    restaurante[cont][2].append(distancia) # coloqueio valor da distancia como terceiro indice das coordenadas 

    restaurante[cont].append([input('digite o numero de pedido: ')])
    
    restaurante[cont].append(input('Digite o numero telefone: '))
    
    cardapio_selecionado = int(input('Digite o cardapio 0 para tradicional 1 para vegano: '))# seleciona qual cardapio
    restaurante[cont].append(cardapios[cardapio_selecionado])#adiciona o cardapio seecionado  

    
    dados = restaurante[cont]
    dados_carregados.append(dados)
    save_json_file('export','arquivo',dados_carregados)

    print('restaurante adicionado')
    print( restaurante[cont])  
    cont += 1

dados_carregados = load_json_file('export','arquivo')
menor_distancia = dados_carregados[0][2][2]
for i in dados_carregados:
    if int(i[2][2]) > menor_distancia:
        pass
    else:
        menor_distancia = i[2][2]
        restaurante_mais_proximo = i[0:3]

print(f'O restaurante mais proximo é: {restaurante_mais_proximo[1]}, codigo: {restaurante_mais_proximo[0]}, distancia: {restaurante_mais_proximo[2][2]}')













    






