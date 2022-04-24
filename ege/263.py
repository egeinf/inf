f = open('26.txt')
n, q = map(int, f.readline().split())

a = []
sA = 0
for line in f:
    data = line.split()
    price, count, t = int(data[0]), int(data[1]), data[2]
    if t == 'A':
        sA += count * price
    else:
        a.append([price, count])


a.sort()
free = Q - sA
i = -1
sB = 0
kB = 0
while sB <= free:
    i += 1
    sB += a[i][0] * a[i][1]
    kB += a[i][1]

sB -= a[i][0] * a[i][1]
kB -= a[i][1]

k = (free - sB) // a[i][0]
kB += k
sB += k * a[i][0]