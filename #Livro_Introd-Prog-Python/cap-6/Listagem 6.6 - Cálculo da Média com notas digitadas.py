print('=' * 72)
print('{:=^72}'.format(' Listagem 6.5 '))
print('{:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' Listagem 6.6 - Cálculo da Média com notas digitadas '))
print('=' * 72)
print('')

notas = [0, 0, 0, 0, 0]

soma = 0
x = 0

while x < 5:
    notas[x] = float(input('Nota %d: ' % x))
    soma += notas[x]
    x += 1
x = 0

while x < 5:
    print('Nota %d: %6.2f' % (x, notas[x]))
    x += 1
print('Média:   %5.2f' % (soma / x))
