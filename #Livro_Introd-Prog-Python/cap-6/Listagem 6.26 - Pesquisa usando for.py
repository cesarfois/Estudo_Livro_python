print('=' * 72)
print('{:=^72}'.format(' Listagem 6.26 '))
print('{:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' Listagem 6.26 - Pesquisa usando for '))
print('=' * 72)
print('')

L = [7, 8, 9, 15]

p = int(input("Digite um numero a pesquisar: "))

for e in L:
    if e == p:
        print("Elemento encontrado!")
        break
else:
    print("Elemento não encontrado.")