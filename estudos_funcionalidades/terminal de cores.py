print('\033[31m ola mundo')
print('\033[7;31;47m ola mundo!\033[m')
a=3
b=5
#print('os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a,b))
#print('os valores são {}{}{} e {}{}{}'.format('\033[32m',a,'\033[m','\033[31m',b,'\033[m'))
cores={'limpo':'\033[m',
       'azul':'\033[34m',
       'amarelo':'\033[33m',
       'pretoebranco':'\033[7;30m'}
print('os valores são {}{}{} e {}{}{}'.format(cores['azul'],a,'\033[m','\033[31m',b,'\033[m'))
