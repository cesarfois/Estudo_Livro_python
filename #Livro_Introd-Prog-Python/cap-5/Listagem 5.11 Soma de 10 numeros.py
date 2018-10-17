print('=' * 72)
print('{0:=^72}'.format(' Listagem 5.11 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' Soma de 10 numeros '))
print('=' * 72)
print('')

n = 1
soma = 0

while n <= 10:
    x = int(input('Digite o %d numero: ' % n))
    soma = soma + x
    n = n + 1
print('Soma: %d' % soma)
