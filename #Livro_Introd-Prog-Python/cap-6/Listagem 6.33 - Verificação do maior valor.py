print('=' * 72)
print('{:=^72}'.format(' Listagem 6.33 '))
print('{:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' Listagem 6.33 - Verificação do maior valor '))
print('=' * 72)
print('')

L = [5, 9, 13, 4]
maximo = L[0]

for e in L:
    if e > maximo:
        maximo = e
print(maximo)
