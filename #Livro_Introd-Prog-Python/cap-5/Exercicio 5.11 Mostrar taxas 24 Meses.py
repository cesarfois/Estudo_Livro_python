print('='*72)
print('{0:=^72}'.format(' Exercicio 5.11 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Mostrar taxas 24 Meses '))
print('='*72)
print('')

mes = 1
deposito_inicial = float(input('Qual é o deposito inicial: '))
taxa_de_juros = float(input('Qual é a taxa de juros: '))
saldo  =  deposito_inicial
juros = 0

while mes <= 24:
    juros = (saldo * (taxa_de_juros / 100))
    saldo = saldo + juros
    print("Os juros ganhos no mês %d = %d , com Saldo = %5.2f" % (mes,juros,saldo))
    mes += 1
print('O total de juros ganhos no periodo = %.2f'%(saldo - deposito_inicial))
print('O total de juros ganhos no periodo = {:.2f}'.format(saldo - deposito_inicial))