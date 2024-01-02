v1 = list()
while True:
   n1 = int(input('digite um valor: '))
   if n1 not in v1:
      v1.append(n1)
      print ('valor adicionado com sucesso')
   else:
        print ('valor duplicado, não adicionarei a lista')
   rsp = str(input('quer continuar ? [S/N] ')).strip().upper()[0]
   if rsp in 'nN':
      break
print (f'a lista em ordem crescente ficaria {sorted(v1)}')