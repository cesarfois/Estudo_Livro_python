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
        self.assertEqual(len('a'), 1)

    def test_len_string_two_characters(self):
        self.assertEqual(len('AB'), 2)

    def test_len_string_Empty(self):
        self.assertEqual(len(''), 0)

    def test_len_string_many_characters(self):
         self.assertEqual(len('o rato roe a roupa'), 18)


if __name__ == '__main__':
    unittest.main()
