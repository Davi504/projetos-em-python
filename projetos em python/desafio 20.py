# esse programa lê o nome de uma pessoa e responde algumas questões
v1 = str (input('digite o seu nome completo :')).strip()
print ('seu nome em maiusculo é {}'.format(v1.upper()))
print ('seu nome em minusculo é {}'.format(v1.lower()))
print ('seu nome tem ao todo {} letras'.format(len(v1)-v1.count(' ')))
sep = v1.split()
print ('seu primeiro é nome {} e tem tantas letras {}'.format(sep[0], len(sep[0])))



