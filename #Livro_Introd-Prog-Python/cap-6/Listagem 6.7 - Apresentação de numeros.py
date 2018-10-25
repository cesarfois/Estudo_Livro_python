print('=' * 72)
print('{:=^72}'.format(' Listagem 6.7 '))
print('{:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' Listagem 6.7 - Apresentação de Numeros'))
print('=' * 72)
print('')

numeros = [0, 0, 0, 0, 0]

x = 0

while x < 5:
    numeros[x] = float(input('Numero %d: ' % (x+1)))
    x += 1

while True:
    escolhido = int(input('Que posição você quer imprimir (0 para sair):'))
    if escolhido == 0:
        break
    print('Você escolheu o numero: %d' % (numeros[escolhido-1]))
