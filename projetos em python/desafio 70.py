#organizando em tabela
listagem = ('celular', 1500,
            'fone', 150,
            'notebook', 2000,
            'tablet', 1300,
            'carregador', 70,
            'televisâo', 3000,
            'video game', 3600)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print (f'{listagem[pos]:.<30}', end='')
    else:
        print (f'R${listagem[pos]:>7.2f}')
