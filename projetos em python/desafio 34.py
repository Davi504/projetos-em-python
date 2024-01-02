#lendo duas notas de um aluno e vendo se ele é reprovado fica de recuperação ou é aprovado
n1 = float (input('digite a primeira nota do aluno : '))
n2 = float (input('digite o valor da segunda nota : '))
media = (n1 + n2) / 2
print ('a média foi de {:.2f}'.format(media))
if media < 5.0 :
    print ('REPROVADO')
elif media >= 5.0 and media < 6.9:
    print ('RECUPERAÇÃO')
elif media >= 7.0:
    print ('APROVADO')