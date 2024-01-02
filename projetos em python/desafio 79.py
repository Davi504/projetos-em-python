totnum = [[], []]
n1 = 0
for c in range(0, 7):
   n1 = int (input('digite um valor: '))
   if n1 % 2 == 0:
      totnum[0].append(n1)
   else:
      totnum[1].append(n1)
print (f'todos os valores {totnum}')
print (f'pares em ordem crescente {sorted(totnum[0])}')
print (f'impares em ordem crescente {sorted(totnum[1])}')
