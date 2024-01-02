from time import sleep
cont = 0
while True:
    print ('caso queira encerrar digite um número negativo')
    sleep(1)
    n1 = int (input('digite qual número deseja ver a tabuada de qual número ? '))
    if n1 < 0:
        break
    while cont < 10:
        cont += 1
        tb = n1 * cont
        print (f'{n1} x {cont} = {tb}')
        sleep (1)