print('=' * 72)
print('{:=^72}'.format(' Listagem 6.37 '))
print('{:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' Listagem 6.37 - Lendo e imprimindo um lista de compras '))
print('=' * 72)
print('')

compras = []

while True:
    produto = input("Produto: ")
    if produto == "fim":
        break
    compras.append(produto)
for p in compras:
    print(p)
print(compras)
