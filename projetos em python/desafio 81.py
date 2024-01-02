matriz = [[0,0,0], [0,0,0], [0,0,0]]
par = mai = scol = 0
for l in range (0, 3):
    for c in range (0, 3):
        matriz = int (input(f'digite o valor para {l}, {c}'))
for l in range(0,3):
    for c in range (0,3):
        print (f'[{matriz[l][c]}]', end='')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
    print ()
print (f'a soma dos valores pares é {par}')
for l in range (0, 3):
    scol += matriz[l][2]
print (f'a soma dos valores da terceira coluna é {scol}')
for c in range (0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz [1][c] > mai:
        matriz[1][c]
print(f'o maior valor da segunda linha é {mai}')
