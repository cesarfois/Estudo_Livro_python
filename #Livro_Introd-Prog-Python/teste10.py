
n = int(input())

matriz = [0]*n
for e in range(n):

    for i in range(1,n - 1):
        matriz[i] = [1] * n
    for r in range(1, n - 1):
        matriz[i][r] = 2


for c in range(n):
    print(matriz[c])


