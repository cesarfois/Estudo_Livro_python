print('='*101)
print('+'*40, 'Operações 2 numeros','+'*40)
print('='*101)

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
print('='*101)
print('Seleccione a operação:\n(1) SOMA\n(2) SUBSTRAÇÃO\n(3) MULTIPLICAÇÃO\n(4) DIVISÃO')
print()
opera = int(input('Que operação deseja fazer: '))

if opera == 1:
   resultado = num1 + num2
elif opera == 2:
    resultado = num1 - num2
elif opera == 3:
    resultado = num1 * num2
elif opera == 4:
    resultado = num1 / num2
else:
    print('Operação invalida!! \n Digite um numero de 0 a 4')
    opera = 0

print('O resultado da operação escolhida é igual a: %.1f' % resultado)
