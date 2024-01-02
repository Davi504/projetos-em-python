alunos = []
while True:
    nome = str (input('digite o nome do aluno: '))
    nota1 = float (input('digite a primeira nota do aluno: '))
    nota2 = float (input('digite a segunda nota do aluno: '))
    media = (nota1 + nota2) / 2 
    alunos.append([nome, [nota1, nota2], media])
    rsp = str (input('deseja continuar ? [S/N] ')).strip()[0]
    if rsp in 'nN':
        break
for i, a in enumerate (alunos):
    print (f'{i:<4}{a[0]:<10}{a[2]:>8.2f}')
while True:
    opc = int (input('deseja mostrar a nota de qual aluno ? (999 encerra o programa)'))
    if opc == 999:
        break
    if opc <= len(alunos) - 1:
        print (f' notas de {alunos[opc][0]}, são {alunos[opc][1]}')