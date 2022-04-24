######################################### перевод числа в СИ
value = 1000
sys = 16
result = ''
while value != 0:
    result = str(value % sys) + result
    value = value // sys
print(result)

######################################### узнать все делители числа
x1 = 200
for i in range(x1, 0, -1):
    if (x1 % i == 0):
        print(i)

######################################### проверить число на одинаковые цифры
value = '1111'
print(len(value) == value.count(value[0]))

######################################### 120 молоко
n = 0
d = set()
st = 0
s = 'МОЛОКО'
for a in s:
    for b in s:
        for c in s:
            for k in s:
                for e in s:
                    for f in s:
                        st = a + b + c + k + e + f
                        if st.count('М') == s.count('М'):
                            if st.count('О') == s.count('О'):
                                if st.count('Л') == s.count('Л'):
                                    if st.count('К') == s.count('К'):
                                        d.add(st)
print(d)
print(len(d))

######################################### степени двойки
n = 12312
a = 1
k = 0
while a < n:
    k = k * 1
    a = a * 2
if a == n:
    print('Число есть в степени двойки')
else:
    print('Число не степень двойки')


######################################### узнать длину самого длинного числа из строчки
def fun(x):
    a = 0
    while x > 0:
        a += 1
        x //= 10
    return a


max_value = 0
value1 = '123 123456'
value1 = value1.split()
for i in value1:
    if fun(int(i)) > max_value:
        max_value = fun(int(i))
print(max_value)


######################################### сколько цифр на 34 ; 59 из числа 1 с помощью програм состоящих из 6 команд
# +1 +2 *2
def f1(n, end, k):
    if n > end or k > 6:
        return 0
    if n == end:
        return 1
    return f1(n + 1, end, k + 1) + f1(n + 2, end, k + 1) + f1(n * 2, end, k + 1)


count = 0


def m(n1, n2):
    global count
    for x in range(n1, n2 + 1):
        if f1(1, x, 0) != 0:
            count += 1


m(34, 59)
print(count)

######################################### есть цифровой диапозон от 1045 до 8963
# найти количество чисел которые а) делятся на 5 б) делятся на 7 в) не делятся на 11 13 17 19 (не кратны им) и минимальное число
count = 0
min_count = 0
for i in range(1045, 8963 + 1):
    if i % 5 == 0:
        if i % 7 == 0:
            if i % 11 != 0:
                if i % 13 != 0:
                    if i % 17 != 0:
                        if i % 19 != 0:
                            count += 1
                            if min_count == 0:
                                min_count = i
print(min_count)
print(count)


######################################### делители
def f2(n):
    k = 1
    d = 2
    n = 0
    while n > d * d:
        if n % d == 0:
            k = k + 2
            d = d + 1
            if k > 2:
                break
    if n == d * d:
        k = k + 1
    if k == 2:
        return 1
    else:
        return 0


for x in range(10):
    print(f2(x))

for i in range(191600, 192020 + 1):
    if f2(i) == 1:
        d = 2
        while i > d * d:
            if i % d == 0:
                print(i, i // d)
            d = d + 1


######################################### делители 2
def f3(n):
    d = 2
    k = 1
    while n > d * d:
        if n % d == 0:
            k = k + 1
            break
        d = d + 1
    if d * d == n:
        k = k + 1
    if k > 1:
        return 0
    else:
        return 1


print(f3(31))
print(f3(6))


######################################### делители 3
def f4(n):
    k = 0
    d = 2
    while n > d * d:
        if n % d == 0:
            k += 2
        d = d + 1
        if k > 2:
            break
    if n == d * d:
        k += 1
    if k == 2:
        return 1
    else:
        return 0


print(f4(5))
for i in range(190201, 190220 + 1):
    if f4(i) == 1:
        d = 2
        while i > d * d:
            if i % d == 0:
                print(i, i // d)
                break
            d = d + 1


######################################### делители 4
def f5(n):
    d = 2;
    k = 1
    while n > d * d:
        if n % d == 0:
            k += 1
            break
        d = d + 1
    if d * d == n:
        k = k + 1
    if k > 1:
        return 0
    else:
        return 1


print(f5(31))
print(f5(6))
t = 1
for i in range(3532000, 3532160 + 1):
    if f5(i) == 1:
        print(t, i)
        t = t + 1


######################################### делители 5
def f6(n):
    d = 2;
    k = 1
    while n > d * d:
        if n % d == 0:
            k += 1
            break
        d = d + 1
    if d * d == n:
        k = k + 1
    if k > 1:
        return 0
    else:
        return 1


print(f(31))
print(f(6))
t = 1
for i in range(3532000, 3532160 + 1):
    if f6(i) == 1:
        print(t, i)
        t = t + 1

######################################### явлется ли слово полиндром
a = '123'
if a[::1] == a[::-1]:
    print('yes')
else:
    print('no')

######################################### задача со строками
a = '123'
print(a[0::2] + a[1::2])

######################################### перестановка первой и последней цифры
a1 = 123
a = a1
k = 0
m = 1
while a > 0:
    k = k + 1
    b = a % 10
    a = a // 10
    m = m * 10
c = a1 % 10
x = a1 % (m // 10) // 10
y = x * 10 + b + c * (m // 10)
print('Первая цифра:', b)
print('Последняя цифра:', c)
print('Результат', y)
print(' ')

######################################### Последовательность до нуля, оканчивается на 3

a = []
x = int(input())
k = 0
while x != 0:
    a.append(x)
    x = int(input())

for x in range(len(a)):
    if a[x] % 10 == 3:
        k += 1

print(k)

#################################### Поиск и замена подстроки
a = ['12324','123453453','1234534531']

for x in a:
    if '1' in x:
        x = x.replace('1', 'test')
        print(x)