<<<<<<< Updated upstream
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = 0
for i in range(n):
    for j in range(i+1, n):
        s = a[i] + a[j]
        if s % 7 == 0:
            k += 1
print(k)
###########################################
# Контрольная сумма R
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
r = int(input())
v = 0
for i in range(n):
    for j in range(i+1, n):
        p = a[i] * a[j]
        if p % 14 == 0 and p > v:
            v = p
print(v)
if r == v:
    print('yes')
######## датчик, 15 секунд, мин. нечет. произведение
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

min = 999999999999999999
for i in range(n):
    for j in range(i+15, n):
        p = a[i] * a[j]
        if p % 2 != 0 and p < min:
            min = p
if min == 999999999999999999:
    min = -1
print(min)
######### Менее 5 расстояние
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = 0
for i in range(n):
    for j in range(i+1, min(i+5, n)):
        if a[i] * a[j] % 14 == 0:
            k += 1
print(k)
######### ai > aj, максимальная сумма температур m = 244, k = 20
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
max = -1
for i in range(n):
    for j in range(i+1, n):
        if a[i] > a[j]:
            s = a[i] + a[j]
            if s % 244 = 20 and s > max:
                max = s
                a = a[i]
                b = a[j]
print(a, b)
#############
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
max = -1
for i in range(n):
    for j in range(i+1, n):
        for p in range(j+1, n):
            s = a[i] + a[j] + a[p]
print(a, b)
##################################### минимальная сумма из всех пар и не делится
f = open('27.txt')
n = int(f.readline())
a = []
for i in range(n):
    b, c = map(int, f.readline().split())
    a.append([b,c])
min = 9999999999
for v0 in a[0]:
    for v1 a[1]:
        for v2 in a[2]:
            for v3 in a[3]:
                for v4 in a[4]:
                    for v5 in a[5]:
                        s = v0 + v1 + v2 + v3 + v4 + v5
                        if s % 3 != 0 and s < min:
                            min = s
print(min)
######################### непрерывные подпоследовательностей сумма кратна 999
f = open('27.txt')
n = int(f.readline())
a = []
for i in range(n):
    a.append(int(f.readline()))
k = 0
for i in range(n):
    for j in range(i, n):
        s = sum(a[i:j+1])
        if s % 999:
            k += 1
print(k)
##########################
=======
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = 0
for i in range(n):
    for j in range(i+1, n):
        s = a[i] + a[j]
        if s % 7 == 0:
            k += 1
print(k)
###########################################
# Контрольная сумма R
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
r = int(input())
v = 0
for i in range(n):
    for j in range(i+1, n):
        p = a[i] * a[j]
        if p % 14 == 0 and p > v:
            v = p
print(v)
if r == v:
    print('yes')
######## датчик, 15 секунд, мин. нечет. произведение
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

min = 999999999999999999
for i in range(n):
    for j in range(i+15, n):
        p = a[i] * a[j]
        if p % 2 != 0 and p < min:
            min = p
if min == 999999999999999999:
    min = -1
print(min)
######### Менее 5 расстояние
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = 0
for i in range(n):
    for j in range(i+1, min(i+5, n)):
        if a[i] * a[j] % 14 == 0:
            k += 1
print(k)
######### ai > aj, максимальная сумма температур m = 244, k = 20
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
max = -1
for i in range(n):
    for j in range(i+1, n):
        if a[i] > a[j]:
            s = a[i] + a[j]
            if s % 244 = 20 and s > max:
                max = s
                a = a[i]
                b = a[j]
print(a, b)
#############
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
max = -1
for i in range(n):
    for j in range(i+1, n):
        for p in range(j+1, n):
            s = a[i] + a[j] + a[p]
print(a, b)
##################################### минимальная сумма из всех пар и не делится
f = open('27.txt')
n = int(f.readline())
a = []
for i in range(n):
    b, c = map(int, f.readline().split())
    a.append([b,c])
min = 9999999999
for v0 in a[0]:
    for v1 a[1]:
        for v2 in a[2]:
            for v3 in a[3]:
                for v4 in a[4]:
                    for v5 in a[5]:
                        s = v0 + v1 + v2 + v3 + v4 + v5
                        if s % 3 != 0 and s < min:
                            min = s
print(min)
######################### непрерывные подпоследовательностей сумма кратна 999
f = open('27.txt')
n = int(f.readline())
a = []
for i in range(n):
    a.append(int(f.readline()))
k = 0
for i in range(n):
    for j in range(i, n):
        s = sum(a[i:j+1])
        if s % 999:
            k += 1
print(k)
##########################
>>>>>>> Stashed changes
