import os 

import os 
import json


def load_json_file(folder_name, file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, folder_name, file_name + '.json')
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as f:
        data = json.load(f)
        result = []
        for restaurant in data:
            id = restaurant['id']
            nome_restaurante = restaurant['nome']
            localizacao = restaurant['localizacao']
            n_pedidos = restaurant['pedidos']
            telefone = restaurant['telefone']
            cardapio = restaurant['cardapio']
            #restaurante_mais_proximo = restaurant['restaurante_mais_proximo']
            result.append([id,nome_restaurante,localizacao, n_pedidos,telefone,cardapio])
        return result

def save_json_file(folder_name, file_name, data):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, folder_name, file_name + '.json')
    data_json = [{'id': id,
                    'nome': nome,
                    'localizacao': localizacao,
                    'pedidos': pedidos,
                    'telefone': telefone,
                    'cardapio': cardapio
                    #'restaurante_mais_proximo':restaurante_mais_proximo
                    } for id,nome, localizacao, pedidos,telefone,cardapio in data]
    with open(file_path, 'w') as f:
        json.dump(data_json, f, indent=4)