print('=' * 72)
print('{:=^72}'.format(' Listagem 6.25 '))
print('{:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' Listagem 6.25 - Impressão de todos os elementos da lista com while.py '))
print('=' * 72)
print('')

L = [8, 9, 15]
x = 0
while x < len(L):
    e = L[x]
    print(e)
    x += 1
