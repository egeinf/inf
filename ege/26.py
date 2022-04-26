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

# Проверка что число есть в списке
def binarySearch(a, x):
    if a[0] > x: return -1

    left = 0
    right = len(a)
    while right > left + 1:
        m = (left + right) // 2
        if x < a[m]:
            right = m
        else:
            left = m

    if a[left] == x:
        return left
    else:
        return -1


a = [3, 6, -8, 8]
a.sort()

print(binarySearch(a, 8))