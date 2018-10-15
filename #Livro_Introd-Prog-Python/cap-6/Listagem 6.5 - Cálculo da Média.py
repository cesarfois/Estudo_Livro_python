print('='*72)
print('{0:=^72}'.format(' Listagem 6.6 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Cálculo de Médi com notas Digitadas '))
print('='*72)
print('')

nota = [2, 3, 4, 5, 6, 7]

somanotas = 0
qtdenotas = 0

for e in nota:
    qtdenotas += 1
    print('Nota %d: %d' % (qtdenotas, e))
    somanotas += e

print('\nA Media das notas: %.2f' % (somanotas/qtdenotas))

