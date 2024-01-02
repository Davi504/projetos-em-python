from time import sleep
def contador (i,f,p):
    print (f'contagem de {i} até o {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print (f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print ('FIM')
    else: 
        cont = i
        while cont >= f:
            print (f'{cont} ', end='',flush= True)
            sleep (0.5)
            cont -= p
        print ('FIM')


contador (1, 10, 1)
contador (10, 0, 2)
print ('agora é sua vez')
ini = int(input('inico: '))
fim = int (input('fim: '))
pas = int (input('passo: '))
contador (ini, fim, pas)
