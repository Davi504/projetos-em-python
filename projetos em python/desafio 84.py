aluno = {}
aluno['nome']= str (input('digite o nome do aluno: '))
aluno['media'] = float (input(f'qual foi a média de {aluno["nome"]}: '))
if aluno['media'] < 6:
    print(f'o aluno(a) {aluno["nome"]} foi reprovado por que sua media de {aluno["media"]} é menor que 6.0')
else:
    print (f'o aluno(a) {aluno["nome"]} foi aprovado por que sua média de {aluno["media"]} é maior que 6.0')
