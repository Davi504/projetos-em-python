#super progressão aritimetica
p1 = int (input('primeiro termo: '))
r = int (input('digite a razão da pa: '))
termo = p1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print ('{} ->'.format(termo), end= '')
        termo += r
        cont += 1
    print(' PAUSA ')
    mais = int (input('quantos termos você quer mostrar a mais: '))
print ('fim')