from datetime import date
adn = int (input('digite o ano de nascimento do atleta: '))
idade = date.today().year - adn
print ('o atleta tem {} anos'.format(idade))
if idade <= 9:
    print ('MIRIM')
elif idade > 9 and idade < 14:
    print ('INFANTIL')
elif idade >= 14 and idade <= 19:
    print ('JUNIOR')
elif idade >= 19:
    print ('SÊNIOR')
elif idade >= 20:
    print ('MASTER')