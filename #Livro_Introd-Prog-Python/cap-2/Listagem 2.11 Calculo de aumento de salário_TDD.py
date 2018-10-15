print('=' * 72)
print('{0:=^72}'.format(' Listagem 2,11 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('=' * 72)
print('\n' * 1)

salario = 1500
aumento = 5


def func_aumento_salario():
    aumento_salario = (salario + (salario * aumento / 100))
    print(aumento_salario)


func_aumento_salario()

assert 1575 == (salario + (salario * aumento / 100))
