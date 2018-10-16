print('='*72)
print('{0:=^72}'.format(' Listagem 9.1 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Abrindo, Lendo e fechando um arquivo  '))
print('='*72)
print()

arquivo = open('numeros.txt', "r")
for linha in arquivo.readlines():
    print(linha)

arquivo.close()
