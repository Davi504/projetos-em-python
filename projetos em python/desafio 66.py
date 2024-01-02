#valor por extenso
n1 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int (input('digite um número de 0 a 20: '))
    if 0 <= num <= 20:
        break
    print ('digite apenas um número de 0 a 20')
print (f'você digitou o número o número {n1[num]}') 