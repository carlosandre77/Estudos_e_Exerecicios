# Métodos em instancias de classes Python

class Carro:
    def __init__(self, nome='Sei lá'):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} esta acelerando...')

fusca = Carro('Fusca')
print(fusca.nome)

celta = Carro('Celta')
print(celta.nome)
celta.acelerar()