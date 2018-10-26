print('=' * 72)
print('{:=^72}'.format(' Listagem 6.42 '))
print('{:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' Listagem 6.42 - Impressão das Compras '))
print('=' * 72)
print('')

produto1 = ["maça", 10, 0.30]
produto2 = ["pera", 5, 0.87]
produto3 = ["kiwi", 6, 0.90]
compras = [produto1, produto2, produto3]

for e in compras:
    print("Produto: %s" % e[0])
    print("Quantidade: %d" % e[1])
    print("Preço: %5.2f" % e[2])
    print()
