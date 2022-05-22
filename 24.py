f = open("24.txt").readline()
max1 = 0
k = 0
for line in range(0, len(f), 2):
    if (f[line-1] == 'A' and f[line] == 'C') or (f[line-1] == 'A' and f[line] == 'B'):
        k += 1
        if k > max1:
            max1 = k
    else:
        k = 0
print(max1)