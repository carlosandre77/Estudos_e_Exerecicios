""" closure e funções que retornam outras funçoes """ 

def criar_saldacao(saudacao, nome):
    def saudar():
        return f'{saudacao},{nome}'
    return saudar


s1 = criar_saldacao('bom dia', 'luis')
s2 = criar_saldacao('Boa noite','luiz')

print(s1)
print(s2()  )
