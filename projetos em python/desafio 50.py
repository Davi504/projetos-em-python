soma = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ' '
totm20 = 0
for p in range (1, 5):
    print ('-----{}° PESSOA -----'.format(p))
    nome = str (input('Nome: ')).strip()
    idade = int (input('Idade: '))
    sexo = str (input('sexo [M//F]; ')).strip()
    somaidade = soma + idade
    if p == 1 and sexo in 'mM':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'mM' and idade > maioridadehomem:
        maioridade = idade
        nomevelho = nome
    if sexo in 'fF' and idade < 20:
        totm20 = totm20 + 1
mediaidade = somaidade / 4
print ('a média de idade do grupo foi de {}'.format(mediaidade))
print ('o homem mais velho tem {} anos e se chama {}'.format(maioridade, nomevelho))
print ('ao todo {} mulheres tem menos de 20 anos'.format(totm20))