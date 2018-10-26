print('=' * 72)
print('{:=^72}'.format(' Listagem 6.31 '))
print('{:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' Listagem 6.31 - Impressão de indices sem usar a função enumerate '))
print('=' * 72)
print('')


L = [5, 9, 13]
x = 0
for e in L:
    print("[%d] %d" % (x, e))
    x += 1