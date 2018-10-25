print('=' * 72)
print('{:=^72}'.format(' Listagem 6.5 '))
print('{:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' Cálculo de Média '))
print('=' * 72)
print('')

notas = [6, 7, 5, 8, 9]

soma = 0
x = 0


while x < 5:
    soma += notas[x]
    x += 1

print('Média: %10.2f' % (soma/x))

