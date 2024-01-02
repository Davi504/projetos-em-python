n1 = (int(input('digite um número: ')),
      int(input('digite outro número: ')),
      int(input('digite mais um número: ')),
      int(input('digite o ultimo número: ')))
print (f'você digitou os valores {n1}')
print (f'o numero nove apareceu {n1.count(9)}')
if 3 in n1:
        print (f'o numero três apareceu na {n1.index(3)+1} posição')
else:
      print ('o valor 3 não foi digitado')
print ('os valores pares digitados foram ', end='')
for n in n1:
       if n % 2 == 0:
              print (n, end=' ')

