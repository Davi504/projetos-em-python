time = []
clube = {}
partidas = []
while True:
    clube.clear()
    clube['nome'] = str (input('Nome: '))
    tot = int (input(f'quantas partidas {clube["nome"]} jogou ? '))
    partidas.clear()
    for c in range(1,tot + 1):
        partidas.append(int(input(f'quantos gols na partida {c}: ')))
    clube['gols'] = partidas[:]
    clube['totgol'] = sum(partidas)
    time.append(clube.copy())
    while True:
        rps = str (input('deseja continuar ? [S/N] ')).upper()[0]
        if rps in 'SN':
            break
        print('digite apenas sim ou não [S/N]')
    if rps == 'N':
        break
print ('=-'*30)
print('cod', end='')
for i in clube.keys():
    print (f'{i:<15}', end='')
print ()
print('=-'* 20)
for k, v in enumerate(time):
    print (f'{k:>3} ', end='')
    for d in v.values():
        print (f'{str(d):<15}', end='')
    print()
print ('=-'*20)
while True:
    busc = int (input('mostrar dados de qual jogador ? (999 para parar)'))
    if busc == 999:
        break
    if busc >= len(time):
        print (f'erro, não existe jogador com o código {busc} ')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busc]["nome"]}: ')
        for i, g in enumerate(time[busc]['gols']):
            print (f'    no jogo {i+1}, fez {g} gols')
    print ('=-'*30)
print ('volte sempre !')
