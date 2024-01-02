temp = []
principal = []
maior = menor = 0
while True:
    temp.append (str(input('Nome: ')))
    temp.append (float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temp [1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    rsp = str (input('quer continuar ? [S/N] ')).strip()[0]
    principal.append (temp[:])
    temp.clear()
    if rsp in 'Nn':
        break
print (f'as pessoas cadastadas foram {principal}')
print (f'o total de cadastro foram de {len(principal)}')
print (f'o maior peso foi de {maior}Kg')
print (f'o menor peso foi de {menor}Kg')
