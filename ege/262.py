f = open('26.txt')
n = int(f.readline())

a = []
for line in f:
    a.append(list(map(int, line.split())))

a.sort()
k = 1
max = -1
r = -1
for i in range(1, len(a)):
    if a[i][0] == a[i-1][0] and a[i][1] == a[i-1][1]+1:
        k += 1
    elif not( a[i][0] == a[i-1][0] and a[i][1] == a[i-1][1]+1 ):
        k = 1
    if k > max:
        max = k
        r = a[i][0]
print(max, r)