print('=' * 72)
print('{:=^72}'.format(' Listagem 6.32 '))
print('{:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' Listagem 6.31 - Impressão de indices usando a função enumerate '))
print('=' * 72)
print('')


L = [5, 9, 13]

for x, e in enumerate(L):
    print("[%d] %d" % (x, e))