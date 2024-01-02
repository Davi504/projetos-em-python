from time import sleep
print ('=-='*20)
print ('CALCULADORA')
print ('=-='*20)
usuario1 = int (input('digite um número: '))
usuario2 = int (input('digite outro número: '))
operadores = 0
while operadores != 5:
    print (''' digite o valor referente a opercão que queira realizar
    [1] somar
    [2] multiplicar
    [3] ver qual é o maior e o menor
    [4] novos números 
    [5] sair do programa''')
    operadores = int (input('digite o numero do operador: '))
    #somando
    if operadores == 1:
        resultado = usuario1 + usuario2
        print('o resultado da soma de {} com {} deu {}'.format(usuario1, usuario2, resultado))
    #multiplicando
    elif operadores == 2:
        resultado = usuario1 * usuario2
        print('a multiplicação de {} com {} deu {}'.format(usuario1, usuario2, resultado))
    #vendo qual é o maior
    elif operadores == 3:
        if usuario1 > usuario2:
            print('o maior número é {}'.format(usuario1))
        else:
            print('o maior número é {}'.format(usuario2))
    #novos números
    elif operadores == 4:
        print ('informe os números novamente')
        usuario1 = int (input('digite o primeiro valor: '))
        usuario2 = int (input('digite o segundo valor: '))
    #finalizando operção
    elif operadores == 5:
        print ('finalizando.....')
        sleep(4)
    else:
        print('opção inválida, tente novamente')
    print ('=-=' * 20)
    sleep(3)
print ('fim do programa volte sempre')
