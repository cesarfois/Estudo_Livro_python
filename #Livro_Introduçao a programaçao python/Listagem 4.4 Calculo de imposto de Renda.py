print('='*72)
print('{0:=^72}'.format(' Listagem 3,17 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Calculo de imposte de renda '))
print('='*72)
print('')

salario = float(input('Digite o salario para calculo do imposto: '))
base = salario
imposto = 0

if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)

print('Salario: R$ %6.2f \n Imposto a pagar: R$ %6.2f \n' %(salario, imposto))
print('Salario: R$: {0:<.0f} \nImposto a pagar: {0:>50.2f}'.format(salario, imposto))
