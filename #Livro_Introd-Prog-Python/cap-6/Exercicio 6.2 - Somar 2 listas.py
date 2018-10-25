print('=' * 72)
print('{:=^72}'.format(' Exercicio 6.2 '))
print('{:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' Exercicio 6.2 - Somar 2 listas '))
print('=' * 72)
print('')

LA = []
LB = []

while True:
    n = int(input("Digite os itens da primeira lista A(0 sai): "))
    if n == 0:
        break
    LA.append(n)
x = 0

while x < len(LA):
    print('Elementos da lista A', LA[x])
    x += 1

while True:
    n = int(input("Digite os itens da primeira lista B (0 sai): "))
    if n == 0:
        break
    LB.append(n)
x = 0

while x < len(LB):
    print('Elementos da lista B', LB[x])
    x += 1
x = 0

LC = LA + LB

while x < len(LC):
    print('Elementos da lista C', LC[x])
    x += 1