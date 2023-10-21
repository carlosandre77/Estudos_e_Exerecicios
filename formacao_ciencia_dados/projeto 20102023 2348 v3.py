# Função para cadastrar restaurante
def cadastrar_restaurante():
  id_restaurante = input('Número de identificação do restaurante: ')

  # validar de entrada única, impedindo id duplicado
  for lista in lista_restaurantes:
    for elemento in lista:
      if id_restaurante == elemento:
        id_restaurante = input('Já existe um restaurante cadastrado com esse ID. Informe novo número de identificação para o restaurante: ')
  
  nome_restaurante = input('Nome do novo restaurante: ')
  lat = input('Digite a latitude: ')
  long = input('Digite a longitude: ')
  n_pedidos = None
  cadastro_completo = [id_restaurante, nome_restaurante, [lat, long], n_pedidos]
  return cadastro_completo

# Função para imprimir as informações do restaurante
def imprimir_cadastro(id):
  for lista in lista_restaurantes:
    for elemento in lista:
      if elemento == id:
        for elemento in lista:
          print(elemento)
        

# variável do tipo lista para reunir os restaurantes cadastrados
lista_restaurantes = []

while True:
  iniciar_cadastro = input('Deseja cadastrar novo restaurante (S - sim; N - não): ').upper()

  # validação de entrada 
  while (not iniciar_cadastro == 'N' and not iniciar_cadastro == 'S') or not iniciar_cadastro.isalpha():
    iniciar_cadastro = input('Opção inválida. Deseja cadastrar novo restaurante (S - sim; N - não): ').upper()
  
  if iniciar_cadastro == 'S':
    informacoes_reunidas = cadastrar_restaurante()
    lista_restaurantes.append(informacoes_reunidas)
  else:
    break

mostrar_qual_cadastro = input('Digite o número id: ')
imprimir_cadastro(mostrar_qual_cadastro)

