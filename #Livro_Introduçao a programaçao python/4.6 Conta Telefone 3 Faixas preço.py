print('='*59)
print('+'*20, 'PREÇO PASSAGEM KM', '+'*20)
print('='*59)
print()

minutos = int(input('Quantos minutos quer contratar: '))

if  minutos < 200:
    preco = 0.20
if minutos >= 200 and minutos <= 400:

    preco = 0.18
else:
    preco = 0.15

print('Valor total do plano: %6.2f' % ( preco * minutos) )