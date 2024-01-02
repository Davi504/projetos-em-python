#esse programa le a velocidade de um carro e informa o valor da multa que ele deve receber considerando 7R$ pra cada km acima do limite
velocidade = float (input('digite a velocidade do carro KM/H: '))
if velocidade > 80:
    vdm = (velocidade - 80) * 7
    print('você foi multado, o valor da multa é {:.2f}R$'.format(vdm))
else:
    print ('você não foi multado, siga sua viagem com segurança')
