print('='*72)
print('{0:=^72}'.format(' Listagem 5.15 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Impressão de Tabuadas'))
print('='*72)
print('')

tabuada = 1
while tabuada <= 10:
    numero = 1
    while numero <= 10:
        print("%d x %2d = %d" %(tabuada, numero, tabuada * numero))
        numero += 1
    tabuada += 1
    print()