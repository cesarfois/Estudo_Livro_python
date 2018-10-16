print('='*72)
print('='*72)
print('{0:=^72}'.format(' Listagem 9.1 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Abrindo, Escrevendo e fechando um arquivo  '))
print('='*72)
print()

arquivo = open('numeros.txt', "w")
for linha in range(1, 101):
    arquivo.write("%d\n" % linha)

arquivo.close()
