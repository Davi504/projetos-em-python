from datetime import date
pessoasmaiores = 0
pessoasmenores = 0
for c in range (1, 8):
    adn = int (input('digite em que ano a {}° nasceu: '.format(c)))
    idade = date.today().year - adn
    if idade >= 18:
        pessoasmaiores += 1
    else:
        pessoasmenores += 1
print ('ao todo tivemos {} pessoas menores e {} pessoas maiores de idade'.format(pessoasmenores, pessoasmaiores))
       
