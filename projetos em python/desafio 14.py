# esse programa vai ler um número decimal e mostrar o seu valor int
from math import floor
v1 = float (input('digite um número:'))
v2 = floor(v1)
print ('o número {} tem a parte inteira {}'.format (v1, v2))
