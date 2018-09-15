print('='*72)
print('='*29,'Listagem 3,12','='*29)
print('='*27,'By César J. Fois','='*27)
print('='*72)

print('Manipulação de composição string')
print('='*72)
print('')


nome = 'joão'
idade = 22
grana = 51.34
print('%s tem %d anos e R$ %f no bolso.' %(nome, idade, grana))
print()
print('%12s tem %3d anos e R$ %5.2f no bolso.' % (nome, idade, grana))
print()
print('%12s tem %-3d anos e R$ %-5.2f no bolso.'% (nome, idade, grana))

