#calculando novo preço do produto
produto = float (input('digite o preço do produto R$: '))
print('''opcão 1: a vista
opção 2: a vista no cartão
opção 3: 2x no cartão
opção 4: 3x ou mais no cartão''')
pgm = int (input('digite a opção :'))
if pgm == 1:
    np = produto - (produto/100) * 10
    print ('o novo preço é de {:.2f}'.format(np))
elif pgm == 2:
    np = produto - (produto/100) * 5
    print ('o novo preço é de {:.2f}'.format(np))
elif pgm == 3:
    np = produto/2
    print ('você pagará duas parcelas de {:2.f}}'.format(np))
elif pgm == 4:
    pcl = int (input('digite quantas parcelas irá querer : '))
    np = ((produto/100) * 20) + produto
    np2 = np / pcl
    print ('você pagara {} parcelas de {:.2f}'.format(pcl, np2))
    