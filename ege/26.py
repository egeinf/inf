f = open('26.txt')
n = int(f.readline())

a = []
for line in f:
    b, c = map(int, line.split())
    a.append([b,c])
a.sort()
r = -1
w = -1
for i in range(1, len(a)):
    if a[i][0] == a[i-1][0] and a[i][1] == a[i-1][1] + 3:
        if a[i][0] != r:
            w = a[i-1][1] + 1
            r = a[i][0]

print(r, w)