cont = 0
soma = 0
while True:
    n1 = int (input('digite um número: [999] pra parar '))
    if n1 == 999:
        break
    cont += 1
    soma += n1
print (f'a soma foi de {soma} e foram digitados {cont} números')
 