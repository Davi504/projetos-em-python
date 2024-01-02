# podem ou não formar triângulo
r1 = float (input('digite o valor do primeiro segmento : '))
r2 = float (input('digite o valor do segundo segmento: '))
r3 = float (input('digite o valor do terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print ('os segmentos acima podem formar triângulo')
else:
    print ('os segmentos acima não podem formar um triãngulo')


