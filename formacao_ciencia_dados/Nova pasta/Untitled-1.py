
from manipulate_data import load_json_file,save_json_file


restaurant = [['Restaurante test', ['test','lat'], 'Telefone 9999', 'Especialidade test','emailtest@gmail.com'],['Restaurante A', 'Endereço A', 'Telefone A', 'Especialidade A'], ['Restaurante B', 'Endereço A', 'Telefone B', 'Especialidade B']]
restaurant.append(['restaurante mec','rua 22','8888888','test'])




column_name = ['Nome', 'Endereço', 'Telefone', 'Especialidade','email']
# Salva a lista no arquivo JSON
save_json_file('cadastro', 'restaurant', restaurant, column_name)
# Carrega a lista do arquivo JSON
result = load_json_file('cadastro', 'restaurant')

print(restaurant)