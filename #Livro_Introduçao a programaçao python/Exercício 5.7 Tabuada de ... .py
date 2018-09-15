print('='*72)
print('{0:=^72}'.format(' Exercício 5.7 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Tabuada de ..  '))
print('='*72)
print('')

n = int(input('Tabuade de: \n'))
inicio = int(input('Digite o Inicio: '))
fim = int(input('Digite o fim: '))

x = inicio
while x <= fim:
    print('%d x %2d = %3d' %(n, x, (n * x)))
    x = x + 1
