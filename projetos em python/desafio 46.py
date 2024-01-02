#vendo se um  número é ou não numero primo
n1 = int (input('digite um número: '))
tot = 0
for c in range (1,  n1 + 1):
    if n1 % c == 0:
        print('\033[33m',end= ' ')
        tot = tot + 1
    else:
        print ('\033[31m',end= ' ')
    print ('{}'.format (c), end= ' ')
print ('o número {} foi divisiel {} vezes'.format (n1,tot))
if tot == 2:
    print ('é número primo ')
else:
    print('não é um número primo')