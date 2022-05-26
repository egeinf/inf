def f(x, y, p):
    if x + y >= 77 or p > 3: return p == 3
    return f(x, y, p + 1) or f(x, y, p + 1)
for s in range(1, 69):
    if f1(7, s, 1):
        print(s, end=' ')
# 20
def f(x, y, p):
    if x + y >= 77 or p > 4: return p == 4
    if p % 2 != 0:
        return f(x, y, p + 1) or f(x, y, p + 1)
    else:
        return f(x, y, p + 1) and f(x, y, p + 1)
#21
def f(x, y, p):
    if x + y >= 77 or p > 5: return p == 3 or p == 5
    if p % 2 == 0:
        return f(x, y, p + 1) or f(x, y, p + 1)
    else:
        return f(x, y, p + 1) and f(x, y, p + 1)