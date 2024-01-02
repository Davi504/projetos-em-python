galera = []
pessoa = {}
soma = media = 0
#adicionando pessoas dentro de um dicionario e adicionando o dicionario a uma lista
while True:
    pessoa.clear
    pessoa['nome'] = str (input('nome: '))
    while True:
        pessoa['sexo'] = str (input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print ('erro !!,pessoa por favor, digite apenas M ou F ')
    pessoa['idade'] = int (input('digite a idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        rsp = str (input('deseja continuar ? [S/N] ')).strip().upper()[0]
        if rsp in 'SN':
            break 
        print ('digite apenas S ou N')
    if rsp == 'N':
        break 
print ('-=' * 20)
print (f'ao todo temos {len(galera)} pessoas cadastradas')
print ('=-'*20)
media = soma / len(galera)
print(f'a media de idade foi de {media:.2f} anos')
print ('=-'*20)
print ('as mulheres castradas foram ', end='')
for p in galera:
    if p['sexo'] in 'fF':
        print (f'{p["nome"]} ', end='')
print ()
print ('=-'*20)
print ('lista de pessoas que estão acima da media: ', end='')
for p in galera:
    if p['idade'] >= media:
        print (f'{p['nome']}')
print()
print ('-='*20)
