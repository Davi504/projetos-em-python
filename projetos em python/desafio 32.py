#diz se um numero é maior menor ou igual
n1 = int (input('digite o primeiro número: '))
n2 = int (input('digite o segundo número: '))
#maior
if n1 > n2:
    print ('o número {} é maior'.format(n1))
elif n2 > n1:
    print('o número {} é maior'.format(n2))
else:
    print ('os valores são iguais')