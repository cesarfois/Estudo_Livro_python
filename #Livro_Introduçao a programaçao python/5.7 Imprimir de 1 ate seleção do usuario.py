print('='*72)
print('{0:=^72}'.format(' Listagem 5.7 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Impressão de números pares de 0 até escolha do usuário While'))
print('='*72)
print('')


fim = int(input('Digite o fim do contador: '))

x = 0
while x <= fim:
    if x % 2 == 0:
        print(x)
    x = x + 1
