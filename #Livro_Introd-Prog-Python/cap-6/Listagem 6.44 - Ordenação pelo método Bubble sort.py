print('=' * 72)
print('{:=^72}'.format(' Listagem 6.44 '))
print('{:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' Listagem 6.44 - Ordenação pelo método Bubble sort '))
print('=' * 72)
print('')

L = [7, 4, 3, 12, 9]
fim = 5

while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if L[x] > L[x + 1]:
            trocou = True
            temp = L[x]
            L[x] = L[x+1]
            L[x+1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1
for e in L:
    print(e)
print()
print(L)