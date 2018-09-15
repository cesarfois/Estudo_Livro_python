print('='*72)
print('{0:=^72}'.format(' Exercício 4.9 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Aprovação de Emprestimo '))
print('='*72)
print('')



valor_casa = int(input('Valor da Casa: '))
salario = int(input('Salario: '))
qtde_parcelas = int(input('Numero de parcelas: '))
valor_parcela = valor_casa/qtde_parcelas

if valor_parcela < (salario * 30)/100:
    print('O emprestimo foi Aprovado')
else:
    print('O Emprestimo foi reprovado')
