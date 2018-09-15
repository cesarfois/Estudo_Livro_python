print('='*72)
print('{0:=^72}'.format(' Listagem 5.19 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Tabuada simples '))
print('='*72)
print('')


t = int(input('\nDigite tabuada de: '))

x = 0

while x <= 10:
    #print("%2d x %2d = %3d" %(t , x, t*x))
    print("{:2} x {:2} = {:3}".format( t, x, t*x ))

    x = x + 1