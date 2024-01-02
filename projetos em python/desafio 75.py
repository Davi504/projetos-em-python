cont = 0
n1 = []
while True:
    n1.append (int(input('digite um valor: ')))
    cont += 1
    rsp = str (input('deseja continuar ? [S/N] ')).strip()[0]
    if rsp in 'nN':
        break
print(f'foram digitados {cont} valores')
n1.sort(reverse=True)
print (f'os valores de forma decrescente são {n1} ')
if 5 in n1:
    print ('o valor 5 está na lista')
else:
    print('o valor 5 não está na lista')