from datetime import date
adn = int (input('informe o seu ano de nascimento: '))
idade = date.today().year - adn
print ('sua idade é {}'.format(idade))
if idade < 18:
    print ('você ainda vai se alistar')
elif idade == 18:
    print ('está na hora de se alistar')
elif idade > 18:
    print ('ja passou a hora de se alistar')
