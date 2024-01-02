#mostrando as vogais
palavras = ('aprender', 'programar', 'linguagem', 'python',
          'curso', 'gratis', 'estudar', 'praticar',
          'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nna palavra {p} temos', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')