print('='*72)
print('{0:=^72}'.format(' Exercício 4.6 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Preço Passagem KM '))
print('='*72)
print('')


dist = int(input('Qual distança da viagem: '))

if dist <= 200:
    preco_passagem = dist * 0.50
else:
    preco_passagem = dist * 0.45

print('Preço da passagem: R$ %.2f' % preco_passagem)


