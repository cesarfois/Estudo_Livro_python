print('='*72)
print('{0:=^72}'.format(' Exercício 3.15 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Cigarro fumado x Dia '))
print('='*72)
print('')

cigarros =  int(input('Quantos cigarro fuma diaramente: '))
anos = int(input('Quantos anos voce já fumou: '))
totalcigarros = (cigarros * 365) * anos
tempoperdido = totalcigarros * 10

print('O tempo de vida perdido: %d minutos ou %d horas ou %d dias' %(tempoperdido, tempoperdido/60, tempoperdido/3600))