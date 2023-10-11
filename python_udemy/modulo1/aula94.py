"""
lista de listas e seus indices
"""
salas = [
    ['Maria','Helena',],
    ['Eliane,',],
    ['Luiz', 'João', 'Eduarda',(0, 10, 20, 30, 40)],
]

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)