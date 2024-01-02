#esse programa mostra o aumento do salário de um funcionário considerando aumento de 15%
v1 = float(input('informe o salário do funcionário R$: '))
v2 = (v1 / 100) * 15
print ('o salário do funcionário era de {} e agora é de {:.2f}.'.format(v1, v1 + v2))
