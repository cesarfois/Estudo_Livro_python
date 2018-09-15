print('='*72)
print('{0:=^72}'.format(' Listagem 4.7 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Categoria x preço'))
print('='*72)
print('')

categoria = int(input('Digite a categoria escolida: '))

if categoria == 1:
    preco = 10.00
else:
    if categoria == 2:
        preco = 20.00
    else:
        if categoria == 3:
            preco = 30.00
        else:
            if categoria == 4:
                preco = 40.00
            else:
                if categoria == 5:
                   preco = 50.00
                else:
                    print('CATEGORIA INVALIDA !! Digite um numero de 1 a 5')
                    preco = 0


print('O preço da categoria escolhida e R$% 0.2f' % preco)



