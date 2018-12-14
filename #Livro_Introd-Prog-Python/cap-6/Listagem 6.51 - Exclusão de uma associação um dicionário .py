print('=' * 72)
print('{:=^72}'.format(' Listagem 6.51 '))
print('{:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' Listagem 6.51 - Exclusão de uma associação um dicionário  '))
print('=' * 72)
print('')

tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30,
          "Feijão": 1.50}

print(tabela)
print()

del tabela ["Tomate"]
print(tabela)

