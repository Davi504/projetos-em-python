v1 = []
for c in range (0, 5):
    n = int(input('digite um valor: '))
    if c == 0 or n > v1[-1]:
        v1.append(n)
    else:
        p = 0
        while p < len(v1):
            if n <= v1[p]:
                v1.insert(p, n)
                break
            p += 1
print (f'os valores digitados em ordem foram {v1}')