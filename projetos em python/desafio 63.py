mdi = 0
h = 0
mm20 = 0
while True:
    idade = int (input('digite a idade: '))
    sexo = str (input('digite o sexo: [M/F] ')).strip().upper() [0]
    if idade >= 18:
        mdi += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        mm20 += 1
    usuario = ' '
    while usuario not in 'SN':
        usuario = str (input('deseja continuar ? [S/N] ')).strip().upper() [0]
    if usuario == 'N':
        break
print (f'foram registrados {mdi} maiores de idade, {h} homens e {mm20} mulheres com menos de 20 anos')