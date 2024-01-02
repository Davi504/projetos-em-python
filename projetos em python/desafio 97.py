def ficha(jogo ='desconhecido0', gol=0):
    print (f'o jogador {jogo} fez {gol} no campeonato ')

n = str (input('nome do jogador: '))
g = str (input('numero de gols: '))
if g.isnumeric():
    g = int(g)
else: 
    g=0
if n.strip() == '':
    ficha(gol = g)
else:
    ficha(n, g)