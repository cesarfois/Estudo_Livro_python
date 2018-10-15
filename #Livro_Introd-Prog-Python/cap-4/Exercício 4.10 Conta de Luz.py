print('='*105)
print('+'*40, 'Aprovação de Emprestimo','+'*40)
print('='*105)

instalacao = input('\n   M E N U\n\n(R) Residencial\n(I) Industrial\n(C) Comercio\n\n Digite o tipo de instalação: ')
consumo = int(input('Digite o consumo mensal: '))


if instalacao == "R" and consumo <= 500:
    preco = 0.40
elif instalacao == "R" and consumo > 500:
    preco = 0.65
elif instalacao == "I" and consumo <= 1000:
    preco = 0.55
elif instalacao == "I" and consumo > 1000:
    preco = 0.60
elif instalacao == "C" and consumo <= 5000:
    preco = 0.55
elif instalacao == "C" and consumo > 5000:
    preco = 0.60
else:
    print('Escolha invalida!!!')
    preco = 0

print('O valor a pagar é de : R$ %.2f' % (preco*consumo))