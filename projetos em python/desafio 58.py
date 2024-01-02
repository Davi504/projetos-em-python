n1 = 0
cont = 0
soma = 0
while n1 != 999:
    n1 = int (input('digite um número [999 para parar]: '))
    soma =+ n1
    cont += 1
print ('você digitou {} números e a soma foi de {}'.format(cont - 1,soma - 999))
print ('acabou')