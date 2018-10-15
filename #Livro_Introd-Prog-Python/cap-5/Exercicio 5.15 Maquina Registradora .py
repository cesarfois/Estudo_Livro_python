print('='*72)
print('{0:=^72}'.format(' Exercicio 5.15 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Maquina registradora'))
print('='*72)
print('')

precototal = 0
precoproduto = 0

while True:
    codigo = int(input('Digite o codigo do produto ou (0) pra SAIR: '))

    if codigo == 0:
        break
    elif codigo == 1:
        precoproduto = 0.50
    elif codigo == 2:
        precoproduto = 1.00
    elif codigo == 3:
        precoproduto = 4.00
    elif codigo == 5:
        precoproduto = 7.00
    elif codigo == 9:
        precoproduto = 9.00
    else:
        print('Codigo Inválido')

    if codigo != 0:

        quantidade = int(input('Digite a quantidade comprada: '))
        precototal = precototal + (precoproduto*quantidade)


print('O total da compra é : R$ %.2f' %precototal)
