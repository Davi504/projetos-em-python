n = int (input('digite um número inteiro para saber a tabuada dele: '))
for c in range (1, 11):
    t = n * c
    print ('{} x {} = {}'.format(n, c, t))