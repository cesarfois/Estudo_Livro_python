print('='*72)
print('{0:=^72}'.format(' Listagem 5.6 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Impressão de 1 até um número digitado pelo usuário While'))
print('='*72)
print('')

fim = int(input('Digite o fim do contador: '))

x = 1
while x <= fim:
    print(x)
    x = x + 1
