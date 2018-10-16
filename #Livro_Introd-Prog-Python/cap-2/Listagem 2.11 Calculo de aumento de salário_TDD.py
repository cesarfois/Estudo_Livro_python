
nome = "Listagem 2.11"
autor = "César J. Fois"


def cabecalho(a,b):
    print('=' * 72)
    print('{0:=^72}'.format((' ' + a + ' ')))
    print('{0:=^72}'.format((' ' + b + ' ')))
    print('=' * 72)
    print('=' * 72)
    print('\n' * 1)


cabecalho(nome, autor)

salario = 1500
aumento = 5

def func_aumento_salario():
    aumento_salario = (salario + (salario * aumento / 100))
    print(aumento_salario)


func_aumento_salario()

assert 1575 == (salario + (salario * aumento / 100))
