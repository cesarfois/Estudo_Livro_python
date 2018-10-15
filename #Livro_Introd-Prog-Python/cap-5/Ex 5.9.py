print('='*102)
print('+'*40,' CONTADOR PAR A FIM ','+'*40)
print('='*102)
print()

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
x = 1
r = 0
while x <= num2:

    r = r - num2
    x = x + 1
print('%d / %d = %d' % (num1, num2, r))
