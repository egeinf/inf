def f(n):
    if n == 1: return 3
    if n == 2: return 3
    if n > 2: return 5*f(n-1) - 4*f(n-2)
print(f(15))

# Минимальное значение
def f(n):
    if n == 0: return 0
    if n % 2 == 0: return f(n/2)
    if n % 2 != 0: return 1 + f(n-1)

for n in range(1, 100000):
    if f(n) == 12:
        print(n)
        break

# f(n) g(n)
def f(n):
    if n == 1: return 1
    return 3 * f(n-1) - 3 * g(n-1)
    
def g(n):
    if n == 1: return 1
    return f(n-1) + 2 * g(n-1)
print(f(20))

# Сколько значений
def f(n):
    if n <= 3: return n
    if n % 2 == 0: return 2 * n + f(n - 1)
    return n * n + f(n - 2)
k = 0
for n in range(1, 100+1):
    if f(n) % 3 == 0:
        k += 1
print(k)

# Сколько значений без подсчёта
def F(n):
    if n > 27: return n * n+5 * n+3
    if n % 2 == 0: return F(n+1) + 2*F(n+4)
    if n % 2 != 0: return F(n+2) + F(n+6)
k = 0
for i in range(1001):
    temp = F(i)
    result = 0
    while temp != 0:
        result += temp % 10
        temp //= 10
    if result == 12:
        k += 1
        print(k, i, F(i), result)
