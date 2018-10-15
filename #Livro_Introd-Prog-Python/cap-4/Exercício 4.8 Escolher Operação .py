print('='*72)
print('{0:=^72}'.format(' Exercício 4.8 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Escolhe Operação + - * / '))
print('='*72)
print('')

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
print('='*101)
print('Seleccione a operação:\n(+) SOMA\n(-) SUBSTRAÇÃO\n(*) MULTIPLICAÇÃO\n(/) DIVISÃO')
print()



opera = input('Escolha uma operação: ')

if opera == '+':
   resultado = num1 + num2
elif opera == '-':
    resultado = num1 - num2
elif opera == '*':
    resultado = num1 * num2
elif opera == '/':
    resultado = num1 / num2
else:
    print('Operação invalida!!\n ')
    opera = 0

print('O resultado da operação escolhida é igual a: %.1f' % resultado)
