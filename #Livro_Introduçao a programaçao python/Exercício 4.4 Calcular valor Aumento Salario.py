print('='*72)
print('{0:=^72}'.format(' Exercício 4.4 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Calcular Valor Aumento Salario '))
print('='*72)
print('')


salario = int(input('Digite o valor do seu salario: '))

if salario <= 1250:
    salario = salario + (salario * 0.15)
if salario > 1250:
    salario = salario + (salario * 0.10)

print('Seu novo salario sera de: R$ %.2f' % salario)

