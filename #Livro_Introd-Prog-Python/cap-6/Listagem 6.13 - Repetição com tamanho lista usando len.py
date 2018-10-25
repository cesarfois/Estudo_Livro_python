print('=' * 72)
print('{:=^72}'.format(' Listagem 6.13 '))
print('{:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' Listagem 6.13 - Repetição com tamanho lista usando len '))
print('=' * 72)
print('')

L = [1, 2, 3]

x = 0

while x < len(L):
    print(L[x])
    x += 1
