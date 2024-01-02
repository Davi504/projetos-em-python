clube = {}
partidas = []
clube['nome'] = str (input('Nome: '))
tot = int (input(f'quantas partidas {clube["nome"]} jogou ?'))
for c in range(1,tot + 1):
   partidas.append(int(input(f'quantos gols na partida {c}: ')))
clube['gols'] = partidas[:]
clube['totgol'] = sum(partidas)
print('=-'* 20)
for k, v in clube.items():
   print (f'{k} tem o valor {v}')
print('=-'* 20)
print (f'o jogador {clube["nome"]} jogou {len(clube["gols"])} partidas')
for i, v in enumerate(clube['gols']):
   print(f'na partida {i+1}, fez {v} gols')
print (f'foi um total de {clube["totgol"]} gols')