#esse programa funciona tipo um jogo de advinhação
from time import sleep
from random import randint
computador = randint(0, 5)
usuario = int (input('Digite um número de 0 a 5: '))
print ('PROCESSANDO...')
sleep(5)
print ('pensei no número {}'.format(computador))
if usuario == computador:
    print ('você venceu')
else :
    print ('você perdeu')