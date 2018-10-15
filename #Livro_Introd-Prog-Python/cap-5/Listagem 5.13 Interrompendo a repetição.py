print('='*72)
print('{0:=^72}'.format(' Listagem 5.13 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Multiplicar com simbolo de soma '))
print('='*72)
print('')




s = 0

while True:

    v = int(input('digite um numero para somar ou 0 para sair:'))
    if v==0:
        break
    s = s+v

print(s)
