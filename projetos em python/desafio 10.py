#esse programa lê o valor do produto, depois informa p preço dele com desconto
v1 = float(input('informe o valor do produto R$:'))
v2 = v1 / 100
print ('o valor do produto com desconto é : {:.2f}'.format(v1 -(v2 * 5)))
