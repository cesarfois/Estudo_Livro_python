print('='*72)
print('{0:=^72}'.format(' Listagem 3,7 v2'))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('A função len')
print('='*72)
print()

list_a = ["a", 'AB', '', '"o rato roe a roupa"']

for c in list_a:
    print('Comprimento da String', c, '=', len(c))
    print()

assert 1 == len('a')
assert 2 == len('AB')
assert 0 == len('')
assert 18 == len('o rato roe a roupa')
