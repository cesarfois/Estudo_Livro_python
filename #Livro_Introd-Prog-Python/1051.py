
x2 = float(input())
x = x2 - 2000.00
print(x)
if (x > 0.00) and (x <= 2000.00):
    print('isento')
if(x > 2000.00) and (x <= 3000.00):
    por = 8.00
if (x > 3000.00) and (x <= 4500.00):
    por = 18.00
if x > 4500.00:
    por = 28.00


re = ( x2 * por)/100

print(re)