print('='*72)
print('{0:=^72}'.format(' Listagem 5.8 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Impressão de números pares de 0 até escolha do usuário sem if '))
print('='*72)
print('')

fim = int(input('Digite o fim do contador: '))

x = 0
while x <= fim:
    print(x)
    x = x + 2
