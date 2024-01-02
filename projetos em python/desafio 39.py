# pedra papel tesoura
from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print ('''suas opções:
[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura''')
jogador = int (input('qual é a sua jogada: '))
print ('o computador escolheu {}'.format(itens[computador]))
print ('o jogador escolheu {}'.format(itens[jogador]))
#se o computador jogar pedra
if computador == 0: #pedra
    if jogador == 0:
        print ('empate')
    elif jogador == 1:
        print ('o jogador venceu')
    elif jogador == 2:
        print ('o computador venceu')
    else:
        print ('jogada invalida')
#se o computador jogar papel
elif computador == 1: #papel
    if jogador == 0:
        print ('o computador venceu')
    elif jogador == 1:
        print ('empate')
    elif jogador == 2:
        print ('o jogador venceu')
    else:
        print ('jogada invalida')
#se o computador jogar tesoura
elif computador == 2: #tesoura
    if jogador == 0:
        print ('o jogador venceu')
    elif jogador == 1:
        print ('o computador venceu')
    elif jogador == 2:
        print ('empate')
    else:
        print ('jogada invalida')
