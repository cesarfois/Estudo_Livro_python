print('=' * 72)
print('{:=^72}'.format(' Listagem 6.13 '))
print('{:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' Listagem 6.15 - Adicao de elementos a lista '))
print('=' * 72)
print('')

L = []

while True:
    n = int(input("Digite um numero (0 sai): "))
    if n == 0:
        break
    L.append(n)
x = 0

while x < len(L):
    print(L[x])
    x += 1
