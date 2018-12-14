linha1 = input().split()
linha2 = input().split()
c1 = int(linha1[0])
q1 = int(linha1[1])
v1 = float(linha1[2])

c2 = int(linha2[0])
q2 = int(linha2[1])
v2 = float(linha2[2])

t1 = (q1 * v1) + (q2 * v2)

print("VALOR A PAGAR: R$ %.2f" % t1)
