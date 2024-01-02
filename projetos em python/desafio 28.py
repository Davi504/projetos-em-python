#aumentando salario de funcionarios com base no quanto eles recebem
salario = float (input('digite o valor do salário R$: '))
if salario >= 1250.00:
    aumento = salario + (salario/100) * 10
    print('o novo salário é R${:.2f}'.format(aumento))
else:
    aumento = salario + (salario/100) * 15
    print('o novo salário é de R${:.2f}'.format(aumento))

