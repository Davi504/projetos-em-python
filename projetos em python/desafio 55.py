#fazendo progressão aritmetica utilizando while
p1 = int (input('primeiro termo: '))
r = int (input('digite a razão da pa: '))
termo = p1
cont = 1
while cont <= 10:
    print ('{} ->'.format(termo), end= '')
    termo += r
    cont += 1
print(' FIM ')