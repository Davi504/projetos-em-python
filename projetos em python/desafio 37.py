#calculo do imc 
altura = float (input('digite sua altura: '))
peso = float (input('digite o seu peso: '))
imc = peso / (altura * altura)
print ('seu imc é de {:.1f}'.format(imc))
if imc < 18.5:
    print ('abaixo do peso ideal ')
elif imc >= 18.5 and imc < 25:
    print ('peso ideal')
elif imc >= 25 and imc < 30:
    print ('sobrepeso')
elif imc >= 30 and imc < 40:
    print ('obesidade')
elif imc == 40 or imc > 40:
    print ('obesidade morbida')