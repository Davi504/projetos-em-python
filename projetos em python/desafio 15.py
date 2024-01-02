# calculo de hipotenusa
import math
v1 = float (input('digite a medida do cateto oposto :'))
v2 = float (input('digite o valor do cateto adjacente :'))
hip = math.sqrt(v1 ** 2 + v2 ** 2)
print ('o valor da hipotenusa é {:.2f}'.format(hip))