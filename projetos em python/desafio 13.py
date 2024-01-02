#esse programa informa o valor do aluguel do carro, sabendo que o dia custa R$ 60 e R$ 0.15 por km rodado
v1 = int (input('informe por quantos dias o carro foi alugado :'))
v2 = float (input('informe quantos KM o carro rodou :'))
v3 = 60 * v1
v4 = 0.15 * v2 
v5 = v3 + v4
print ('o valor a ser pago é de :{:.2f} R$'.format(v5))