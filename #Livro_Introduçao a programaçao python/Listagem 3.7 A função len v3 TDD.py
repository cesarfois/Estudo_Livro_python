import unittest

print('='*72)
print('{0:=^72}'.format(' Listagem 3,7 v4 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('A função len')
print('='*72)
print()

list_a = ['a', 'AB', '', 'o rato roe a roupa']

class Len_String():
    for c in list_a:
        print('Comprimento da String', c, '=', len(c))
        print()


class len_String_Test(unittest.TestCase):

    def test_len_string_one_character(self):
        self.assertListEqual([len('a'), len('AB'), len(''), len('o rato roe a roupa')],
                             [1, 2, 0, 18])


if __name__ == '__main__':
    unittest.main()
