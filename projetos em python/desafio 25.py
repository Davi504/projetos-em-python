#calcule o valor da viagem considerando R$ 0.50 por km para viagens até 200km e 0.45 para viagens mais longos
viagem = float (input('digite a distancia da viagem em KM: '))
if viagem <= 200:
    valor = viagem * 0.50
    print ('o valor a ser pago é de R${:.2f}'.format(valor))
else:
    valor = viagem * 0.45
    print ('o valor a ser pago é de R${:.2f}'.format(valor))