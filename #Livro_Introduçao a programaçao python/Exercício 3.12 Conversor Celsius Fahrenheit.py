print('='*72)
print('{0:=^72}'.format(' Exercício 3.12 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Conversor Celsius Fahrenheit '))
print('='*72)
print('')


distancia = int(input('Que distancia vai percorrer: '))
velocidade = int(input('Qual velocidade que vai andar: '))
tempo = distancia/velocidade

print('O tempo da viagem é igual a: %d horas' % tempo)