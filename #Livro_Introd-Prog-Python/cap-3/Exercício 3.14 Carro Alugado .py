print('='*72)
print('{0:=^72}'.format(' Exercício 3.14 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Carro Alugado '))
print('='*72)
print('')

km = int(input('Quantos km percorreu: '))
d = int(input('Quantos dias alugou o carro: '))

total = float((km*0.15) + (d*60))

print('Preço total: R$ %.2f ' %total)