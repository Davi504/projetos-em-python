from datetime import date
empresa = {}
empresa['nome'] = str (input('Nome: '))
nasc = int(input('ano de nascimento: '))
empresa['idade'] = date.today().year - nasc
empresa['clt'] = int (input('carteira de trabalho (0 se bão tiver): '))
if empresa['clt'] != 0:
    empresa['contr'] = int(input('ano de contratação: '))
    empresa['salario'] = float(input('digite o salario: R$ '))
    empresa['aposentadoria'] = empresa['idade'] + ((empresa['contr'] + 35) - date.today().year)
for k, v in empresa.items():
    print (f'{k} tem o valor {v}')