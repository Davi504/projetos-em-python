#aprovando emprestimo
casa = float (input('digite o valor da casa R$: '))
salario = float (input('digite o valor mensal do salário R$: '))
ano = int (input('em quantos anos deseja pagar: '))
meses = ano * 12
vdpc = casa / meses
if vdpc <= (salario/100) * 30:
    print('o seu salario é de R$ {:.2F} e o valor da parcela é de R$ {:.2F}'.format(salario, vdpc))
    print ('seu empréstimo foi aprovado')
elif vdpc >= (salario/100) * 30:
    print ('o valor do seu salário é de R$ {:.2F} e sua parcela ficaria {:.2f}'.format(salario, vdpc))
    print ('seu empréstimo foi negado pois o valor da parcela não pode ser maior que 30 por cento do seu salário')
