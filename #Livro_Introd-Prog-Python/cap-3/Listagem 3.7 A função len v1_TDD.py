print('='*72)
print('{0:=^72}'.format(' Listagem 3,7 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('A função len')
print('='*72)
print('')


print(len('a'))
print('')

print(len('AB'))
print('')


print(len(''))
print()

print(len('o rato roe a roupa'))
print()

assert 1 == len('a')
assert 2 == len('AB')
assert 0 == len('')
assert 18 == len('o rato roe a roupa')
