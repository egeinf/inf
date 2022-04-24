# МНОГО СТРОК
a = open('24.txt')
z = [i.strip() for i in a]

for x in range (len(z)):
    if int(z[x]) % 2 == 0:
        print(z[x])

# 1 СТРОКА | САМАЯ ДЛИННАЯ ЦЕПОЧКА НЕЧЕТНЫХ ЧИСЕЛ КОТОРАЯ ВСЕГДА УВЕЛИЧИВАЕТСЯ
f = open('24.txt')
line = f.readline()

max = 0
k = 0

for i in range(len(line)):
    if int(line[i]) % 2 == 0:
        k = 0
    elif line[i] >= line[i-1]:
        k += 1
    else:
        k = 1

    if k > max:
        max = k
print(max)