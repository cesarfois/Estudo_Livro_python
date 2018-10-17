print('=' * 72)
print('{0:=^72}'.format(' Listagem 5.16 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' Listagem 5.16 Impressão de Tabuadas sem repetições aninhadas '))
print('=' * 72)
print('')

tabuada = 1
numero = 1

while tabuada <= 10:
    while numero <= 10:
        print("%d x %2d = %d" % (tabuada, numero, tabuada * numero))
        numero += 1
    if numero == 11:
        numero = 1
        tabuada += 1
        print()
