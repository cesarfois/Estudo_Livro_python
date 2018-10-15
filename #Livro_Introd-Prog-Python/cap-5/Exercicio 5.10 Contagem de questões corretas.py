print('='*72)
print('{0:=^72}'.format(' Exercicio 5.10 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Contagem de questões corretas '))
print('='*72)
print('')


pontos = 0
questao = 1


while questao <= 3:
    resposta = input('Resposta da questão %d: ' % questao)
    if questao == 1 and (resposta == 'b' or resposta == 'B'):
        pontos = pontos + 1
        if questao == 2 and (resposta == 'a' or resposta == 'A'):
        pontos = pontos + 1
        if questao == 3 and (resposta == 'd' or resposta == 'D'):
        pontos = pontos + 1
    questao += 1
print('O aluno fez %d ponto(s)' %pontos)