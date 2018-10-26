print('=' * 72)
print('{:=^72}'.format(' Listagem 6.34 '))
print('{:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' Listagem 6.34 - Copia de elementos para outras listas '))
print('=' * 72)
print('')

V = [5, 9, 13, 4, 12, 4, 21, 0, 8, 7]
P = []
I = []

for e in V:
    if e % 2 == 0:
        P.append(e)
    else:
        I.append(e)
print("Pares: ", P)
print("Impares: ", I)
