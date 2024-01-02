resp = 's'
cont = 0
soma = 0
maior = 0
menor = 0
while resp in 'sS':
    n1 = int (input('digite um número : '))
    cont += 1
    soma += n1
    if cont == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    resp = str (input('digite se deseja continuar [S/N] ')).upper().strip() [0]
media = soma / cont
print ('a quantidade de números foi de {} e a media entre eles {:.2f}'.format(cont, media))
print ('o maior número foi {}, e o menor foi {}'.format(maior, menor))
