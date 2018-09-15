print('='*72)
print('{0:=^72}'.format(' Listagem 4.8 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Categoria x preço com elif'))
print('='*72)
print('')

categoria = int(input('Digite a categoria escolida: '))

if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 20
elif categoria == 3:
    preco = 30
elif categoria == 4:
    preco = 40
elif categoria == 5:
    preco = 50
else:
    print('CATEGORIA INVALIDA!!!, Digite uma opção de 1 a 5')
    preco = 0


print('O preço da categoria escolhida e R$% 6.2f' % preco)



