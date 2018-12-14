print('=' * 72)
print('{:=^72}'.format(' Listagem 6.48 '))
print('{:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' LListagem 6.48 - Verificação de uma existência numa chave '))
print('=' * 72)
print('')

tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30,
          "Feijão": 1.50}

if "Manga" in tabela:
    print("TEM MANGA")
else:
    print("NAO TEM MANGA")

if "Tomate" in tabela:
    print("TEM TOMATE")
else:
    print("NAO TEM TOMATE")

print()
c = 0
while c < len(tabela):
    print(c)
    c += 1

