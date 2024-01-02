from random import randint
from time import sleep
sorteio = []
jogo = []
usuario = int (input('digite o número de jogos: '))
tot = 1
while tot <= usuario:
    cont = 0
    while True:
        n1 = randint (1, 60)
        if n1 not in sorteio:
            sorteio.append(n1)
            cont += 1
        if cont >= 6:
            break
    sorteio.sort
    jogo.append(sorteio[:])
    sorteio.clear()
    tot += 1
for i, l in enumerate(jogo):
    print (f'jogo {i+1}: {l}')
    sleep (2)
