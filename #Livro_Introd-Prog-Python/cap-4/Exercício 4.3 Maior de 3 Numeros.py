print('='*72)
print('{0:=^72}'.format(' Exercício 4.3 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Maior de 3 Numeros '))
print('='*72)
print('')

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite um numero: '))


if num1 > num2 and num1 > num3:
    maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

if num1 < num2 and num1 < num3:
    menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

print('O numero maior é: %d' % maior)

print('O numero menor é: %d' % menor)








