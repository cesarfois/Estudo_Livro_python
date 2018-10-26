print('=' * 72)
print('{:=^72}'.format(' Exercicio 6.12 '))
print('{:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format('Exercicio 6.12 - Verificação do menor valor '))
print('=' * 72)
print('')

L = [5, 9, 13, 4]
minimo = L[0]

for e in L:
    if e < minimo:
        minimo = e
print(minimo)
