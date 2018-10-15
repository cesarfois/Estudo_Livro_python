print('='*72)
print('{0:=^72}'.format(' Exercício 5.8 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Leia dois numeros e Imprima o Resultado da Multiplicão   '))
print('='*72)
print('')


num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
x = 1
r = 0
while x <= num2:

    r = r + num2
    x = x + 1
print('%d x %d = %d' % (num1, num2, r))
