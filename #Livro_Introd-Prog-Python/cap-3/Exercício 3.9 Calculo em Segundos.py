print('='*72)
print('{0:=^72}'.format(' Exercício 3.9 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Conversor Dias,horas, em Segundos '))
print('='*72)
print('')


d = int(input('Digite Dias: '))
h = int(input('Digite horas: '))
m = int(input('Digite Min: '))
s = int(input('Digite Seg: '))
resultado = d*86400 + h*3600 + m*60 + s

print('O valor em segundos é igual a %d segundos' % resultado)

