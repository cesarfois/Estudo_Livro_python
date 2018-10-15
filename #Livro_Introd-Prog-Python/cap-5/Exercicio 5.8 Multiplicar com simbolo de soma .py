print('='*72)
print('{0:=^72}'.format(' Exercicio 5.8 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Multiplicar com simbolo de soma '))
print('='*72)
print('')

n1 = int(input('\n D igite um numero: '))
n2 = int(input('\n Digite outro numero: '))
print()


x = 1
r = 0

while x <= n1:
      r = r + n2
      x = x + 1
      #print("%2d x %2d = %3d" %(t , x, t*x))
print("{:^3} x {:2} = {:<3}".format( n1, n2, r ))


print()
