print('='*72)
print('{0:=^72}'.format(' Listagem 3,17 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' CARRO NOVO OU VELHO DEPENDENDO DA IDADE '))
print('='*72)
print('')


idade_carro = int(input('Digite a idade do seu Carro: '))



if  idade_carro <= 3:
    print("O seu carro é novo")
if idade_carro > 3:
    print('O Seu carro é velho')

