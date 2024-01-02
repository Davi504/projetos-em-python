us = str (input('digite a expressão: '))
lista = []
for sim in us:
    if sim == '(':
        lista.append('(')
    elif sim == ')':
        if len(lista) > 0:
            lista.pop
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print ('sua expressão está válida ')
else:
    print ('sua expressão está errada ')
