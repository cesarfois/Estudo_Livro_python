print('=' * 72)
print('{0:=^72}'.format(' Exercicio 5.14 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' While & break '))
print('=' * 72)
print('')

s = 0
qn = 0

while True:

    v = int(input('Digite um numero ou 0 para sair: '))

    if v == 0:
        break
    s = s + v
    qn = qn + 1

print(
    "Quantidade de numeros digitados: {}\n"
    "A soma dos numeros digitados = {}\n"
    "A media dos numeros digitados: {}"
        .format(
        qn, s, s / qn))
print("Quantidade de números digitados:", qn)
print("Soma:                           ", s)
print("Média:                     %10.2f" % (s / qn))
