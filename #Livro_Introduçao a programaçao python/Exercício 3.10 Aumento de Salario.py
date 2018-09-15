print('='*72)
print('{0:=^72}'.format(' Exercício 3.10 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Aumento de Salario '))
print('='*72)
print('')

salario =  float(input('Salario: '))
porcentagem = int(input('Aumento em %: '))
salario_com_aumento = salario + (salario*porcentagem/100)

print('O salario com aumento de %d é igual a: R$ %.2f' %(porcentagem, salario_com_aumento))
