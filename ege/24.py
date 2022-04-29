# МНОГО СТРОК
f = open('24.txt')
a = [i.strip() for i in f]

for x in range (len(a)):
    if int(a[x]) % 2 == 0:
        print(a[x])

# 1 СТРОКА | САМАЯ ДЛИННАЯ ЦЕПОЧКА НЕЧЕТНЫХ ЧИСЕЛ КОТОРАЯ ВСЕГДА УВЕЛИЧИВАЕТСЯ
f = open('24.txt').readline()

max = 0
k = 0

for i in range(len(f)):
    if int(f[i]) % 2 == 0:
        k = 0
    elif f[i] >= f[i-1]:
        k += 1
    else:
        k = 1

    if k > max:
        max = k
print(max)
