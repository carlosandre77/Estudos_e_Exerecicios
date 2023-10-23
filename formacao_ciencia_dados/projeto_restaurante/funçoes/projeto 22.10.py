from manipulate_data import load_json_file,save_json_file

def calcular_distancia(localizacao1, localizacao2):
    lat1 = float(localizacao1[0])
    lon1 = float(localizacao1[1])
    lat2 = float(localizacao2[0])
    lon2 = float(localizacao2[1])    
    distancia = ((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2) ** 0.5
    return distancia

def cadastro():
    restaurante = []
    nome_restauramte = input("Digite o nome do restaurante: ")
    lat = float(input("Digite a latitude do restaurante: "))
    long = float(input("Digite a longitude do restaurante: "))
    n_pedidos = int(input("Digite o numero de pedidos: "))
    restaurante.append([nome_restauramte,[lat,long],n_pedidos])
    restaurante[0].append(calcular_distancia([-43.23,5.52],['100','44']))
    return restaurante

restaurante = cadastro()
print(restaurante)


#codigo para carregar e salvar arquivo Json
column_name = ['Nome', 'localizacao','numero de pedidios','distancia']
# Salva a lista no arqu"ivo JSON
save_json_file('cadastro', 'restaurant', restaurante, column_name)
# Carrega a lista do arquivo JSON
result = load_json_file('cadastro', 'restaurant')
