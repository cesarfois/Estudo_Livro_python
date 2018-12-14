print('=' * 72)
print('{:=^72}'.format(' Listagem 6.50 '))
print('{:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' Listagem 6.50 - Obtenção do preço com um dicionário  '))
print('=' * 72)
print('')

tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30,
          "Feijão": 1.50}

while True:
    produto = input("Digite o nome do produto, fim para terminar: ")
    if produto == "fim":
        break
    if produto in tabela:
        print("Preço %5.2f" % tabela[produto])
    else:
        print("Produto não encontrado!")

