total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preço = float (input('Preço>: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    usuario =' '
    while usuario not in 'SN':
        usuario = str (input('deseja continuar ? [S/N]')).strip().upper() [0]
    if usuario == 'N':
        break
print (f'o total da compra foi de R${total:.2f}')
print (f'temos {totmil} produtos custando mais R$1000.00')
print (f'o produto mais barato foi {barato} que custa R${menor:.2f}')
