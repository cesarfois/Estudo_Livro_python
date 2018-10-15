print('='*72)
print('{0:=^72}'.format(' Exercício 5.6 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Tabuada de ..  '))
print('='*72)
print('')

n = int(input('Tabuade de: \n'))

x = 1
while x <= 10:
    print('%d x %2d = %3d' %(n, x, (n * x)))
    x = x + 1
