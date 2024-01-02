def area(a, b):
    area = a * b
    print (f'a aréa de um terreno de {a}x{b} é igual a {area:.2f}m²')


#programa principal

print ('-='*30)
print ('calculo de area')
print ('-='*30)
usuario1 = float (input('LARGURA: '))
usuario2 = float (input('COMPRIMENTO: '))
area(usuario1, usuario2)