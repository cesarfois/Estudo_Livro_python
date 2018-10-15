print('='*72)
print('{0:=^72}'.format(' Exercício 3.11 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Desconto do Produto '))
print('='*72)
print('')


produto =  float(input('Valor do Produto: '))
porcentagem = int(input('Desconto em %: '))
valor_com_desconto = produto - (produto*porcentagem/100)

print('O valor do produto com desconto de %d porcento é igual a: R$ %.2f' %(porcentagem, valor_com_desconto))
