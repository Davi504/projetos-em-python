#desenvolva um programa que lê 6 numeros e some apenas aquels que forem par
soma = 0
cont = 0
for c in range (1, 7):
    n1 = int (input('digite o valor {}: '.format(c)))
    if n1 % 2 == 0:
        soma = soma + n1
        cont = cont + 1
print ('você informou {} números pares e a soma foi {}'.format (cont, soma))