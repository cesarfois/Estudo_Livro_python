n = int(input())

i = 0
out = ""

while i < n:
    i1 = i
    i += 1
    i2 = i
    i3 = i1 + i2
    out = str(i1) + str(i2) + str(i3)
print(out)
