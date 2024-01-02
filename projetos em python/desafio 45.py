#faça um programa que le o primeiro termo e a razão de uma progressâo aritimetica e mostre os 10 primeiros números
n1 = int (input('digite o primeiro termo da progressão: '))
n2 = int (input('digite a razão da progressão: '))
decimo = n1 + (10 - 1) * n2
for c in range(n1, decimo + n2 , n2):
    print (c, end= ' ')