print('='*72)
print('{0:=^72}'.format(' Listagem 5.9 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Listagem 5.10 Contagem de questoes corretas '))
print('='*72)
print('')

pontos = 0
questao = 1

while questao <= 3:
    resposta = input("Resposta da questao %d: " % questao)
    if questao == 1 and resposta == "b":
        pontos = pontos + 1
    if questao == 2 and resposta == "a":
        pontos = pontos + 1
    if questao == 3 and resposta == "b":
        pontos = pontos + 1
    questao +=1
    print("O aluno fez %d ponto(s)" % pontos)