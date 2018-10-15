import unittest

print('='*72)
print('{0:=^72}'.format(' Listagem 3,8 TDD '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('Manipulação de Strings')
print('='*72)
print('')

a = 'ABCDEF'

print(a[0])
print()
print(a[1])
print()
print(a[5])
print()
print(a[3])


class StringsTests(unittest.TestCase):
    def test_strings(self):
        self.assertListEqual([a[0], a[1], a[5], a[3],], ['A','B', 'F', 'D'], "O resultado é diferente" )


if __name__ == '__main__':
    unittest.main()
