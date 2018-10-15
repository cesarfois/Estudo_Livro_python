print('='*72)
print('{0:=^72}'.format(' Exercicio 5.21 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Contagem de Cedulas'))
print('='*72)
print('')

valor = int(input('Digite o valor a pagar: '))

cedulas = 0
atual = 100
apagar = valor

while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        if apagar >= 1:
            print('%d cedula(s) de R$ %d' % (cedulas,atual))
        else:
            print("%d moeda(s) de R$%5.2f" % (cedulas, atual))
        if apagar < 0.01:
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0