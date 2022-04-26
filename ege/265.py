def binarySearch(a, x):
    if a[0] > x: return False

    left = 0
    right = len(a)
    while right > left + 1:
        m = (left + right) // 2
        if x < a[m]:
            right = m
        else:
            left = m

    if a[left] == x:
        return True
    else:
        return False

f = open('a.txt')
n = int(f.readline())
a = []
for line in f:
    a.append(int(line))
a.sort()
k = 0
for i in range(n):
    for j in range(i+1, n):
        if a[i] % 2 == 0 and a[j] % 2 == 0:
            avg = (a[i] + a[j]) // 2
            if binarySearch(a, avg):
                k += 1
print(k)