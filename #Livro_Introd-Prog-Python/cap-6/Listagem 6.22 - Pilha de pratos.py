print('=' * 72)
print('{:=^72}'.format(' Listagem 6.22 '))
print('{:=^72}'.format(' By César J. Fois '))
print('=' * 72)
print('{0:=^72}'.format(' Listagem 6.22 - Pilha de pratos '))
print('=' * 72)
print('')

prato = 5
pilha = list(range(1, prato + 1))

while True:
    print("\nExistem %d pratos na pilha" % len(pilha))
    print("Pilha atual:", pilha)
    print("Digite E para empilhar um novo prato,")
    print("ou D para desempilhar. S para sair.")
    operacao = input("Operação (E, D ou S): ")
    if operacao == 'D':
        if(len(pilha)) > 0:
            lavado = pilha.pop(-1)
            print("Pilha vazia! Nada para lavar.")
        else:
            print("Pilha vazia! Nada para lavar.")
    elif operacao == "E":
        prato += 1 # Novo prato
        pilha.append(prato)
    elif operacao == "S":
        break
    else:
        print("Operação invalida! Digite apenas E, D ou S!")