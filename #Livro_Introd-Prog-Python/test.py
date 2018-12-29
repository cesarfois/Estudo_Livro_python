soma = 0
lin = 12
lin2 = 0

for c in range(12):
    lin = lin - 1
    lin2 = lin2 + 1
    for j in range(12):
        if (j < lin) and (j >= lin2):
            print('%4d' % j, end='|')
            soma = soma + 1
    print()

print(soma)