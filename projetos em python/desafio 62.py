#jogo dp par ou impar
from time import sleep
from random import randint
cont = 0
jogador = int (input('digite 1 se você deseja par e 2 se deseja impar : '))
if jogador == 1:
    while True:
        computador = randint(1, 10)
        jogador = int (input('escolha qual número quer jogar de 1 a 10:'))
        soma = computador + jogador
        cont += 1
        if soma % 2 == 0:
            sleep(1)
            print(f'o computador escolheu {computador} e o jogador escolheu {jogador} e a soma deles foi de {soma} que é par')
            sleep(1)
            print (f'o total de vitorias foi de {cont}')
        else:
            sleep (1)
            print (f'você perdeu, o computador jogou {computador} e você jogou {jogador} e a soma deles {soma} é impar')
            sleep(1)
            print (f'o números de tentativas foi de {cont}')
            break
elif jogador == 2:
    while True:
        computador = randint (1, 10)
        jogador = int (input('escolha qual número quer jogar de 1 a 10: '))
        soma = computador + jogador
        cont += 1
        if soma % 2 != 0:
            sleep(1)
            print(f'você venceu, computador escolheu {computador} e o jogador escolheu {jogador} e a soma deles foi {soma} que é impar')
            sleep(1)
            print (f'o total de vitorias é de {cont}')
        else:
            sleep(1)
            print (f'você perdeu, o computador escolheu {computador}, e o jogador escolheu {jogador} e a soma deles {soma} é par')
            sleep(1)
            print (f'o total de tentativas foi de {cont}')
            break
print ('fim')
