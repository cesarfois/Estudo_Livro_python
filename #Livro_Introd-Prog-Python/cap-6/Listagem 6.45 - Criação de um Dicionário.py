print('=' * 72)
print('{:=^72}'.format(' Listagem 6.45 '))
print('{:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' Listagem 6.45 - Criação de um Dicionário '))
print('=' * 72)
print('')

tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30,
          "Feijão": 1.50}

print(tabela)

print()

print(tabela["Alface"])

tabela["cebola"] = 1.60

print()

print(tabela)