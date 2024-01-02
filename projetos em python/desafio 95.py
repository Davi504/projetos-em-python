from datetime import date
def voto(idade):
    idade = date.today().year - adn
    if idade >= 18 and idade < 65:
        print(f'voce tem {idade} anos e o voto é obrigatorio')
    elif idade < 18 or idade > 65:
        print(f'voce tem {idade} e o voto não é obrigatorio')
    


adn = int (input('digite o ano que você nasceu: '))
print (voto(adn))