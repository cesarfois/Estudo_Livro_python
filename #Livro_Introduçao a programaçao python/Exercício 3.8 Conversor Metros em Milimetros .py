print('='*72)
print('{0:=^72}'.format(' Exercício 3.8 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Conversão M em mm '))
print('='*72)
print('')

M = float(input('Digite o valor em Metros: '))
print('O valor %.1f em militros é igual a: %.0f cm' % (M, (M*1000)))

print('A medida em milimetros =  {0:0.5f}'.format((M * 1000)))

