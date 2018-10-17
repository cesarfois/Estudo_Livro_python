print('=' * 72)
print('{0:=^72}'.format(' Listagem 5.12 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' Calculo de media do acumulador '))
print('=' * 72)
print('')

x = 1
soma = 0

while x <= 5:
    n = int(input('%d Digite o numero: ' % x))
    soma = soma + n
    x = x + 1

print('Media: %5.2f' % (soma/5))
