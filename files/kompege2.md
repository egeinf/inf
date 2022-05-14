https://kompege.ru/variant?kim=25008180

![image](https://user-images.githubusercontent.com/70198995/157410390-1d465914-9e41-4f73-a726-7d3bc016bd5b.png)

1) 47

2) zyxw
```
for x in 0,1:
  for y in 0,1:
    for z in 0,1:
      for w in 0,1:
        F = (w == z) or (x and not y) or w
        if F == 0:
          print(z,y,x,w)
# X X 1 X
# X 0 X X
# X 1 0 0
```
3) 381
4) 20
5) 23
```
def defCount(N):
  N = int(N)
  result = 0
  while N != 0:
    result = result + (N % 10)
    N //= 10
  return result

for N in range(30):
  res_N = N
  two_N = bin(N)[2:]
  
  if res_N % 2 == 0:
    two_N += str(res_N)
  else: two_N = '1' + two_N + '00'
  
  if int(two_N) > 11010111:
    print(res_N)
    break
```
6) 44
```
for s in range(1,10000):
  res_s = s
  n = 1
  while s <= 70:
    s = s + 9
    n = n * 7
  if n == 343:
    print(res_s)
    break
```
7) 1024
```
i = (2 * 1024 * 1024 * 8) // (1024*1536)
print(2**i)
```
8) 
```
count = 0
for a in range(7):
  for b in range(7):
    for c in range(7):
      for d in range(7):
        for e in range(7):
          for f in range(7):
            for g in range(7):
              a = str(a)
              b = str(b)
              c = str(c)
              d = str(d)
              e = str(e)
              f = str(f)
              g = str(g)
              s = a + b + c + d + e + f + g
              if (a != '3') and (a != '5') and ('22' not in s) and ('44' not in s):
                count += 1
print(count)
```
9) [ ]
10) 20
11) 368
```
I = 20 * 4
bite = I / 8
print(((bite + 36) * 8192) / 1024)
```
12) 22
```
s = '2' * 52
while '222' in s or '000' in s:
    if '000' in s:
        s = s.replace('000', '2', 1)
    else:
        s = s.replace('222', '02', 1)
print(s)
```
13) []
14)
```
x = 6 * 512 ** 180 + 7 * 64 ** 181 + 3 * 8 ** 184 + 5 * 8 ** 125 - 65
result = ''
while x != 0:
    result += str(x % 64)
    x //= 64
print(result.count('0'))
19, 20, 21)
```
def f(x, y, p):
    if x + y >= 211 or p > 3:
        return p == 3
    return f(x + 1, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 1, p + 1) or f(x, y * 2, p + 1)
for s in range(1, 193):
    if f(17, s, 1):
        print(s, end=' ')
        break
print()
def f(x, y, p):
    if x + y >= 211 or p > 4:
        return p == 4
    if p % 2 != 0:
        return f(x + 1, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 1, p + 1) or f(x, y * 2, p + 1)
    else:
        return f(x + 1, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 1, p + 1) and f(x, y * 2, p + 1)
for s in range(1, 193):
    if f(17, s, 1):
        print(s, end=' ')
print()
def f(x, y, p):
    if x + y >= 211 or p > 5:
        return p == 3 or p == 5
    if p % 2 == 0:
        return f(x + 1, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 1, p + 1) or f(x, y * 2, p + 1)
    else:
        return f(x + 1, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 1, p + 1) and f(x, y * 2, p + 1)
for s in range(1, 193):
    if f(17, s, 1):
        print(s, end=' ')
        break
```
