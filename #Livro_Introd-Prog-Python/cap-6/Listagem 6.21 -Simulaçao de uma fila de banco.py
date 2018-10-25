print('=' * 72)
print('{:=^72}'.format(' Listagem 6.21 '))
print('{:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' Listagem 6.21 -Simulaçao de uma fila de banco '))
print('=' * 72)
print('')


ultimo = 10
fila = list(range(1, ultimo+1))

while True:
    print("\nExistem %d clientes na fila" % len(fila))
    print('Fila atual: ', fila)
    print('Digite F para adicionar um cliente ao fim da fila,')
    print('ou A para realizar o atendimento. S para sair.')
    operacao = input('Operação (F, A ou S): ')
    if operacao == "A":
        if(len(fila)) > 0:
            atendido = fila.pop(0)
            print('Cliente %d atendido' % atendido)
        else:
            print('Fila vazia! Ninguem para Atender.')
    elif operacao == "F":
        ultimo += 1  # Incrementa o ticket do novo cliente
        fila.append(ultimo)
    elif operacao == "S":
        break
    else:
        print('Operação invalida! Digite apenas F, A ou S!')