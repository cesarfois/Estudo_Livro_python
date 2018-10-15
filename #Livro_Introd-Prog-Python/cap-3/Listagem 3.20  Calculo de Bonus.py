print('='*72)
print('{0:=^72}'.format(' Listagem 3,17 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Calculo de Bonus '))
print('='*72)
print('')


anos = int(input('Anos de serviço: '))
valor_por_ano = float(input('Valor por Ano: '))
bonus = anos * valor_por_ano
print('O bonus é de R$ %5.2f' % bonus)
