f = open('26.txt')
n, q = map(int, f.readline().split())

a = []
pA = []
pB = []
for line in f:
    data = line.split()
    price, t = int(data[0]), data[1]
    a.append(price)
    if t == 'A':
        pA.append(price)
    else:
        pB.append(price)

a.sort()
pA.sort()
pB.sort()
s = 0
i = -1
while s <= Q:
    i += 1
    s += a[i]
k = i
s = sum(pA[:k])
i = i - 1
j = 0
while s > Q:
    s = s - pA[i-j] + pB[j]
    j += 1

print(i + 1 - j, Q - s)