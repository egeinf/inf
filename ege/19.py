# pylint: disable=all
# 1 КУЧА
print('Задача 19:')
def f(x, p):
    if x >= 42 or p > 3: return p == 3
    return f(x + 1, p + 1) or f(x + 3, p + 1) or f(x * 2, p + 1)
for s in range(1, 42):
    if f(s, 1):
        print(s, end=' ')

print('Задача 20:')
def f(x, p):
    if x >= 42 or p > 4: return p == 4
    if p % 2 != 0:
        return f(x + 1, p + 1) or f(x + 3, p + 1) or f(x * 2, p + 1)
    else:
        return f(x + 1, p + 1) and f(x + 3, p + 1) and f(x * 2, p + 1)
for s in range(1, 42):
    if f(s, 1):
        print(s, end=' ')

print('Задача 21:')
def f(x, p):
    if x >= 42 or p > 5: return p == 3 or p == 5
    if p % 2 == 0:
        return f(x + 1, p + 1) or f(x + 3, p + 1) or f(x * 2, p + 1)
    else:
        return f(x + 1, p + 1) and f(x + 3, p + 1) and f(x * 2, p + 1)
for s in range(1, 42):
    if f(s, 1):
        print(s, end=' ')


########################### 2 КУЧИ
print('Задача 19:')
def f(x, y, p):
    if x + y >= 77 or p > 3: return p == 3
    return f1(x + 1, y, p + 1) or f1(x * 2, y, p + 1) or f1(x, y + 1, p + 1) or f1(x, y * 2, p + 1)
for s in range(1, 69):
    if f(7, s, 1):
        print(s, end=' ')
print('Задача 20:')
def f(x, y, p):
    if x + y >= 77 or p > 4: return p == 4
    if p % 2 != 0:
        return f(x + 1, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 1, p + 1) or f(x, y * 2, p + 1)
    else:
        return f(x + 1, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 1, p + 1) and f(x, y * 2, p + 1)
for s in range(1, 69):
    if f2(7, s, 1):
        print(s, end=' ')
print('Задача 21:')
def f(x, y, p):
    if x + y >= 77 or p > 5: return p == 3 or p == 5
    if p % 2 == 0:
        return f(x + 1, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 1, p + 1) or f(x, y * 2, p + 1)
    else:
        return f(x + 1, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 1, p + 1) and f(x, y * 2, p + 1)
for s in range(1, 69):
    if f(7, s, 1):
        print(s, end=' ')
# 2 КУЧИ
print('Задача 19:')
def f(x, y, p):
    if x + y >= 69 or p > 3:
        return p == 3
    return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or f(x * 2, y, p + 1) or f(x, y * 3, p + 1)
for s in range(1, 58):
    if f(10, s, 1):
        print(s, end=' ')
print('Задача 20:')
def f(x, y, p):
    if x + y >= 69 or p > 4:
        return p == 4
    if p % 2 != 0:
        return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or f(x * 2, y, p + 1) or f(x, y * 3, p + 1)
    else:
        return f(x + 1, y, p + 1) and f(x, y + 1, p + 1) and f(x * 2, y, p + 1) and f(x, y * 3, p + 1)
for s in range(1, 58):
    if f(10, s, 1):
        print(s, end=' ')
print('Задача 21:')
def f(x, y, p):
    if x + y >= 69 or p > 5:
        return p == 3 or p == 5
    if p % 2 == 0:
        return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or f(x * 2, y, p + 1) or f(x, y * 3, p + 1)
    else:
        return f(x + 1, y, p + 1) and f(x, y + 1, p + 1) and f(x * 2, y, p + 1) and f(x, y * 3, p + 1)
for s in range(1, 58):
    if f(10, s, 1):
        print(s, end=' ')
