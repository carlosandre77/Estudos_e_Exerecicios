# class - classes são moldes para criar novos objetos
# as classes geeram novos objetos (instancias) que
# podem ter seus propios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# por convição, usamos pascalcase para nomes de classes
# string = 'Luiz' # str
# print(string.upper())
# Print(isinstance(string,str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        

p1 = Pessoa('Luiz','Otavio')

p2 = Pessoa('Maria','joana')

print(p1.sobrenome,p2.nome)