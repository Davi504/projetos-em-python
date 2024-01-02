n1 = []
n2 = []
n3 = []
while True:
    n1.append (int(input('digite um valor: ')))
    rsp = str (input('deseja continuar ? [S/N] ')).strip()[0]
    if rsp in 'nN':
        break
for i, v in enumerate(n1):
    if v % 2 == 0:
        n2.append(v)
    else:
        n3.append (v)
print (f'a lista é {n1}')
print (f'lista de pares {n2}')
print (f'lista de impares {n3}')