#jogo da advinhação 2.0
from random import randint
computador = randint (0, 10)
print ('tente advinhar o número que pensei de 0 a 10')
palpite = 0
acertou = False
while not acertou:
    jogador = int (input('qual é o seu palpite: '))
    palpite = palpite + 1
    if jogador == computador:
        acertou = True
print ('acertou')
print ('{} palpites'>format(palpite))