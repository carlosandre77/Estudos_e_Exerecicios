num= int(input('digite um numero: '))
tot=0
for c in range(1,num+1):
    if num % c==0:
        print('\033[33m',end=" ")
        tot+=1
    else:
        print('\033[31m', end=" ")
    print(c,end='')
if tot==2:
    print('\n {} é primo'.format(num))
else:
    print('\n {} não é primo'.format(num))


