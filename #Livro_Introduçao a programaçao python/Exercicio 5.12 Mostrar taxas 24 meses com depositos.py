print('='*72)
print('{0:=^72}'.format(' Exercicio 5.12 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Mostrar taxas 24 Meses com Depositos '))
print('='*72)
print('')

mes = 1
deposito_inicial = float(input('Qual é o deposito inicial: '))
taxa_de_juros = float(input('Qual é a taxa de juros: '))
investimento = float(input('Qual é o investimento mensal: '))
saldo  =  deposito_inicial
juros = 0

while mes <= 24:
    juros = (saldo * (taxa_de_juros / 100))
    saldo = saldo + juros + investimento
    print("Os juros ganhos no mês %2d = R$ %3.2f , com Saldo = R$ %5.2f" % (mes,juros,saldo))
    mes += 1
print('O total de juros ganhos no periodo = R$ %.2f'%(saldo - deposito_inicial))
print('O total de juros ganhos no periodo = R$ {:.2f}'.format(saldo - deposito_inicial))