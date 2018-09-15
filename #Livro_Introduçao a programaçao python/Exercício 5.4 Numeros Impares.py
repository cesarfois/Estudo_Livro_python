print('='*72)
print('{0:=^72}'.format(' Exercício 5.4 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Numeros Impares '))
print('='*72)
print('')

fim = int(input('Digite o fim do contador: '))

x = 1
while x <= fim:
    print(x)
    x = x + 2
