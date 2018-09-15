print('='*72)
print('{0:=^72}'.format(' Exercício 4.2 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Carro Multa '))
print('='*72)
print('')


vel_carro = int(input('Digite a velocidade do seu Carro: '))
multa_valor = float((vel_carro - 80)*5)



if vel_carro <= 80:
    print("Você esta andando no limite correto de velocidade")
if vel_carro > 80:
    print('VOCE FOI MULTADO!!! \nNo valor de R$ %.2f'% multa_valor)

