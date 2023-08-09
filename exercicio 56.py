"""desenvolva um programa que leia o nome, iadade e sexo de 4 pessoas.
no final mostre:
- a media de idade do grupo
-qual o o homem mais velho         - quantas mulheres tem menos de 20 anos """
idadef=0
sexo1='M'
f_quant=0
velho=0
for c in range(1,4):
    nome=(input(' digite o nome da {}° pessoa: '.format(c)))
    sexo=(input('qual o sexo?: [m] para masculino [f] para feminino: '))
    sexo1=sexo.upper()
    idade=int(input('qual sua idade: '))
    idadef+=idade
    if idade > idadef:
        velho=idade
    if sexo1 == ('F') and idade < 20:
        f_quant+=1
        print(f_quant)
    if sexo1 =='M' and idadef > idade:
        velho=nome
print('tem {} mulheres com menos de 20 anos: '.format(f_quant))
print('o nome do homem mais velho é: ',(velho))
print('a media de idade é: ',(idadef/3))