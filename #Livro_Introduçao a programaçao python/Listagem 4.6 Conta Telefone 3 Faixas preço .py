print('='*72)
print('{0:=^72}'.format(' Listagem 4.6 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Conta de telefone com 3 faixas de preço '))
print('='*72)
print('')

minutos = int(input('Quantos minutos quer contratar: '))

if minutos < 200:
    preco = 0.20
else:
    if minutos < 400:
        preco = 0.18
    else:
        preco = 0.15
print('Valor total do plano: %6.2f' % (preco * minutos))
print('Valor total do plano: {0:6.2f}'.format(preco * minutos))
