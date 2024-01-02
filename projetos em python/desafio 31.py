#escreva um programa que leia um numero inteiro e peça ao usuario qual sera a base de conversao em binario, octal haxadecimal
n1 = int (input('digite um número inteiro :'))
cv = int (input('digite como deseja converter esse número sendo\n1\n para binário 2 para octal\ne 3 para hexadecimal'))
if cv == 1:
    print ('convertido para binario o numero ficaria {}'.format(bin(n1)))
elif cv == 2:
    print ('convertido o numero ficaria {}'.format(oct(n1)))
elif cv == 3:
    print ('convertido o número ficaria {}'.format(hex(n1)))
else: 
    print ('opção invalida')

    