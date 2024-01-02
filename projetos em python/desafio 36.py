r1 = float (input('digite o valor do primeiro segmento : '))
r2 = float (input('digite o valor do segundo segmento: '))
r3 = float (input('digite o valor do terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print ('os segmentos acima podem formar triângulo')
    #equilatero
    if r1 == r2 and r1 == r3:
        print ('equilátero')
    #isosceles
    if r1 == r2 or r1 == r3 or r3 == r2:
        print ('isósceles')
    #escaleno
    if r1 != r2 and r1 != r3 and r3 != r2:
        print ('escaleno')
else:
    print ('os segmentos acima não podem formar um triãngulo')
