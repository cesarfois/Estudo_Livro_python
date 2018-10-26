print('=' * 72)
print('{:=^72}'.format(' Listagem 6.39 '))
print('{:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' Listagem 6.39 - Impressão de uma lista de strings, letra a letra '))
print('=' * 72)
print('')

L = ["maças", "peras", "kiwis"]
for s in L:
    for letra in s:
        print(letra)
print(L)